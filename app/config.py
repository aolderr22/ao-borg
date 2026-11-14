import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "")
MODEL_NAME = os.getenv("FOUNDRY_MODEL_NAME", "")