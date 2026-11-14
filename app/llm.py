import logging
import time
from functools import lru_cache

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from app import config

logger = logging.getLogger(__name__)

@lru_cache
def _client():
    project = AIProjectClient(
        endpoint=config.PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    )
    return project.get_openai_client()

def generate(system: str, user: str) -> str:
    start = time.perf_counter()
    resp = _client().chat.completions.create(
        model=config.MODEL_NAME,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    latency_ms = (time.perf_counter() - start) * 1000
    usage = resp.usage
    logger.info(
        "llm_call model=%s latency_ms=%.0f prompt_tokens=%s completion_tokens=%s",
        config.MODEL_NAME,
        latency_ms,
        usage.prompt_tokens if usage else None,
        usage.completion_tokens if usage else None,
    )
    return resp.choices[0].message.content