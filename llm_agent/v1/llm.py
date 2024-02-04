from langchain_community.llms.ollama import Ollama
from langchain.llms.openai import OpenAI

def get_llm(llm_type: str):
    """Get an LLM."""
    if llm_type == "ollama":
        llm = Ollama()
    elif llm_type == "openai":
        llm = OpenAI()
    return llm