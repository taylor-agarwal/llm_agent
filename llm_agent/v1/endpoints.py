from fastapi import APIRouter
from llm_agent.v1.apispec import InvokeRequest, InvokeResponse
from llm_agent.v1.agents import InternetEnabledAgent

router = APIRouter()

@router.post("/")
def index():
    return "App is running!"


@router.post("/invoke", response_model=InvokeResponse)
def invoke(request: InvokeRequest):
    """Invoke the basic agent."""
    agent = InternetEnabledAgent()
    result = agent.invoke(request=request)

    response = InvokeResponse(response=result)

    return response