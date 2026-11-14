import logging
import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import llm
from app.logging_setup import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="AI-SEA")

SYSTEM_PROMPT = (
    "You are a software requirements analyst. Given a feature request, "
    "summarize it in two sentences and list any obvious ambiguities."
)

class FeatureRequest(BaseModel):
    title: str
    description: str


class FeatureResponse(BaseModel):
    request_id: str
    analysis: str


class RepoRequest(BaseModel):
    path: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/feature-requests", response_model=FeatureResponse)
def create_feature_request(req: FeatureRequest):
    request_id = str(uuid.uuid4())
    logger.info("feature_request received id=%s title=%s", request_id, req.title)
    try:
        analysis = llm.generate(SYSTEM_PROMPT, f"{req.title}\n\n{req.description}")
    except Exception:
        logger.exception("llm call failed id=%s", request_id)
        raise HTTPException(status_code=502, detail="Model call failed")
    return FeatureResponse(request_id=request_id, analysis=analysis)


@app.post("/repo/files")
def list_repo_files(req: RepoRequest):
    root = Path(req.path).expanduser().resolve()
    if not root.is_dir():
        raise HTTPException(status_code=400, detail="Not a directory")
    files = [
        str(p.relative_to(root))
        for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts
    ]
    return {"root": str(root), "file_count": len(files), "files": files[:200]}