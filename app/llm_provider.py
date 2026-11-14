from langchain_openai import ChatOpenAI

def get_primary_generative_model(deployment_model_name, project_endpoint, token_provider):
    return ChatOpenAI(
        model=deployment_model_name,
        base_url=f"{project_endpoint.rstrip('/')}/openai/v1/",
        api_key=token_provider,
        use_responses_api=True,
    )