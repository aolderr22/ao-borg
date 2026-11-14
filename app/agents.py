from langchain.agents import create_agent

def get_requirements_analytics_agent(llm, system_prompt):
    return create_agent(
        model=llm,
        tools=[], # Populate tools list later.
        system_prompt=system_prompt,
        response_format=str,
    )