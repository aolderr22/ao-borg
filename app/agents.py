from langchain.agents import create_agent
from app.schemas import FeatureResponse

def get_requirements_analytics_agent(llm, system_prompt):
    return create_agent(
        model=llm,
        tools=[], # Populate tools list later.
        system_prompt=system_prompt,
        #response_format=FeatureResponse,
    )