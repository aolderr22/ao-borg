import logging
import uuid
import os
from azure.identity import (DefaultAzureCredential, get_bearer_token_provider)
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from pathlib import Path
from fastapi import (FastAPI, HTTPException)
from app.agents import get_requirements_analytics_agent
from app.llm_provider import get_primary_generative_model
from app.logging_setup import setup_logging
from app.prompts import BUSINESS_REQUIREMENTS_SYSTEM_PROMPT
from app.schemas import (FeatureRequest, RepoRequest)

setup_logging()
logger = logging.getLogger(__name__)
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "")
    GENERATIVE_MODEL_NAME = os.getenv("FOUNDRY_GENERATIVE_MODEL_NAME", "")
    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
    )
    primary_generative_model = get_primary_generative_model(GENERATIVE_MODEL_NAME, PROJECT_ENDPOINT, token_provider)
    app.state.primary_generative_model = primary_generative_model
    requirements_analytics_agent = get_requirements_analytics_agent
    app.state.requirements_analytics_agent = requirements_analytics_agent
    yield

    # Shutdown operations
    credential.close()

app = FastAPI(title="AI-SEA", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze_requirements")
def analyze_requirements(req: FeatureRequest):
    result = app.state.requirements_analytics_agent.invoke({
        "messages": [
            {"role": "user", "content": BUSINESS_REQUIREMENTS_SYSTEM_PROMPT}
        ]
    })

    structured_response = result["structured_response"]
    return structured_response