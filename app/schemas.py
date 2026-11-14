from pydantic import BaseModel

class FeatureRequest(BaseModel):
    title: str
    description: str

class RepoRequest(BaseModel):
    path: str