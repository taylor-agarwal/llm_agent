from langchain.prompts import PromptTemplate
from langchain import hub

# From langchain.hub.pull("hwchase17/react")
REACT_AGENT_PROMPT: PromptTemplate = hub.pull("hwchase17/react")