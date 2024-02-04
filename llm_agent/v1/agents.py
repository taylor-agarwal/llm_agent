from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import BaseTool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.language_models import LLM
from langchain.prompts import PromptTemplate

from llm_agent.v1.apispec import InvokeRequest
from llm_agent.v1.llm import get_llm
from llm_agent.v1.prompts import BASE_AGENT_PROMPT

class BaseAgent:

    agent_name: str = "unnamed_agent"
    tools: list[BaseTool] = []
    llm: LLM = None
    prompt: PromptTemplate = None
    agent = None


class InternetEnabledAgent(BaseAgent):

    agent_name: str = "internet_enabled_agent"
    tools: list[BaseTool] = [DuckDuckGoSearchRun()]
    prompt: PromptTemplate = BASE_AGENT_PROMPT
    llm: LLM = get_llm("openai")
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def invoke(self, request: InvokeRequest):
        """Invoke the agent."""
        prompt = request.prompt
        response = self.agent_executor.invoke({"input": prompt})
        print(response)
        return response
        
