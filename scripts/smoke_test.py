import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
client = project.get_openai_client()
resp = client.chat.completions.create(
    model=os.environ["FOUNDRY_MODEL_NAME"],
    messages=[
        {"role": "user", "content": "In one sentence, what is a software requirements specification?"}
    ],
)
print(resp.choices[0].message.content)