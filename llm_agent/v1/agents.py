from langchain.tools import BaseTool
from langchain.agents import create_react_agent, AgentExecutor, initialize_agent, AgentType
from langchain_core.language_models import LLM
from langchain.prompts import PromptTemplate

from llm_agent.v1.apispec import InvokeRequest
from llm_agent.v1.llm import get_llm
from llm_agent.v1.prompts import REACT_AGENT_PROMPT
from llm_agent.v1.toolkits import get_internet_toolkit, get_github_toolkit

class BaseAgent:

    agent_name: str = "unnamed_agent"
    tools: list[BaseTool] = []
    llm: LLM = None
    prompt: PromptTemplate = None
    agent = None


class InternetEnabledAgent(BaseAgent):

    def __init__(self):
        self.agent_name: str = "internet_enabled_agent"
        self.tools: list[BaseTool] = get_internet_toolkit()
        self.prompt: PromptTemplate = REACT_AGENT_PROMPT
        self.llm: LLM = get_llm("ollama")
        agent = create_react_agent(llm=self.llm, tools=self.tools, prompt=self.prompt)
        self.agent = AgentExecutor(agent=agent, tools=self.tools, verbose=True, handle_parsing_errors=True)

    def invoke(self, request: InvokeRequest):
        """Invoke the agent."""
        prompt = request.prompt
        response = self.agent.invoke({"input": prompt})
        print(response)
        return response


class GitHubEnabledAgent(BaseAgent):
    
    def __init__(self):
        self.agent_name: str = "github_enabled_agent"
        self.tools: list[BaseTool] = get_github_toolkit()
        self.llm: LLM = get_llm("ollama-code")
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )

    def invoke(self, request: InvokeRequest):
        """Invoke the agent."""
        prompt = request.prompt
        response = self.agent.run(prompt)
        print(response)
        return response
        
