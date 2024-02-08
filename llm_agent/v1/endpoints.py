from fastapi import APIRouter
from llm_agent.v1.apispec import InvokeRequest, InvokeResponse
from llm_agent.v1.agents import InternetEnabledAgent, GitHubEnabledAgent

router = APIRouter()

@router.post("/")
def index():
    return "App is running!"


@router.post("/internet_agent", response_model=InvokeResponse)
def internet_agent(request: InvokeRequest):
    """Invoke the basic agent."""
    agent = InternetEnabledAgent()
    result = agent.invoke(request=request)
    print(result)

    response = InvokeResponse(response=result)

    return response


@router.post("/github_agent", response_model=InvokeResponse)
def github_agent(request: InvokeRequest):
    """Invoke the basic agent."""
    agent = GitHubEnabledAgent()
    result = agent.invoke(request=request)
    print(result)

    response = InvokeResponse(response=result)

    return response