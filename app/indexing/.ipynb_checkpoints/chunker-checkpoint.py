from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser
from langchain_core.documents import Document

SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", "build", "dist"}
_parser = Parser(Language(tspython.language()))
DEF_TYPES = {"function_definition", "class_definition", "decorated_definition"}

def iter_python_files(root: Path):
    for p in root.rglob("*.py"):
        if not SKIP_DIRS.intersection(p.parts):
            yield p

def _name(node) -> str:
    inner = node.child_by_field_name("definition") or node
    n = inner.child_by_field_name("name")
    return n.text.decode() if n else "<anonymous>"

def chunk_file(path: Path, root: Path) -> list[Document]:
    source = path.read_bytes()
    rel = str(path.relative_to(root))
    docs = []
    for node in _parser.parse(source).root_node.children:
        if node.type in DEF_TYPES:
            docs.append(Document(
                page_content=source[node.start_byte:node.end_byte].decode("utf-8", "replace"),
                metadata={"path": rel, "symbol": _name(node),
                          "start_line": node.start_point[0] + 1,
                          "end_line": node.end_point[0] + 1},
            ))
    if not docs and source.strip():  # scripts with no top-level definitions
        docs.append(Document(page_content=source.decode("utf-8", "replace")[:4000],
                             metadata={"path": rel, "symbol": "<module>",
                                       "start_line": 1, "end_line": source.count(b"\n") + 1}))
    return docs