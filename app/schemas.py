from pydantic import BaseModel

class FeatureRequest(BaseModel):
    title: str
    description: str

class FeatureResponse(BaseModel):
    request_id: int
    analysis: str

class RepoRequest(BaseModel):
    path: str