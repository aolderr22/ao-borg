from langchain_core.tools import tool
from app.indexing.store import get_retriever

@tool
def retrieve_code(query: str) -> str:
    """Search the indexed repository for code relevant to the query.
    Returns matching functions/classes with file paths and line numbers."""
    docs = get_retriever().invoke(query)
    return "\n\n".join(
        f"# {d.metadata['path']}:{d.metadata['start_line']}-{d.metadata['end_line']} "
        f"({d.metadata['symbol']})\n{d.page_content}" for d in docs)