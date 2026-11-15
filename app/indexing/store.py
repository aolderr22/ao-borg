import os
from pathlib import Path
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.indexing.chunker import iter_python_files, chunk_file
# reuse the same endpoint value and token_provider as your LLM factory
from app.auth import token_provider
from app.config import PROJECT_ENDPOINT

def _store() -> Chroma:
    emb = OpenAIEmbeddings(
        model=os.environ["FOUNDRY_EMBEDDING_NAME"],
        base_url=f"{PROJECT_ENDPOINT.rstrip('/')}/openai/v1/",
        api_key=token_provider,
    )
    return Chroma(collection_name="repo_code", embedding_function=emb,
                  persist_directory="./chroma_db")

def index_repo(repo_path: str) -> int:
    root = Path(repo_path).resolve()
    docs = [d for f in iter_python_files(root) for d in chunk_file(f, root)]
    ids = [f"{d.metadata['path']}:{d.metadata['symbol']}:{d.metadata['start_line']}" for d in docs]
    _store().add_documents(docs, ids=ids)   # stable ids prevent duplicates on re-index
    return len(docs)

def get_retriever(k: int = 5):
    return _store().as_retriever(search_kwargs={"k": k})