import os
from pathlib import Path
from urllib.parse import urlparse
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.indexing.chunker import iter_python_files, chunk_file

CHROMA_DIR = Path(__file__).resolve().parents[2] / "chroma_db"   # always the project root

def get_embeddings(token_provider) -> OpenAIEmbeddings:
    # Embeddings use the resource-level endpoint, not the project-scoped one.
    host = urlparse(os.environ["FOUNDRY_PROJECT_ENDPOINT"]).hostname
    return OpenAIEmbeddings(
        model=os.environ["FOUNDRY_EMBEDDING_MODEL_NAME"],
        base_url=f"https://{host}/openai/v1/",
        api_key=token_provider,
        check_embedding_ctx_length=False,
    )


def _store(token_provider) -> Chroma:
    return Chroma(
        collection_name="repo_code",
        embedding_function=get_embeddings(token_provider),
        persist_directory=str(CHROMA_DIR),
    )


def index_repo(repo_path: str, token_provider) -> int:
    root = Path(repo_path).resolve()
    print("root", root)
    docs = [d for f in iter_python_files(root) for d in chunk_file(f, root)]
    ids = [f"{d.metadata['path']}:{d.metadata['symbol']}:{d.metadata['start_line']}" for d in docs]
    _store(token_provider).add_documents(docs, ids=ids)   # stable ids prevent duplicates on re-index
    return len(docs)


def get_retriever(token_provider, k: int = 5):
    return _store(token_provider).as_retriever(search_kwargs={"k": k})