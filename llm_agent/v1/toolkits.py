def get_internet_toolkit():
    from langchain_community.tools import DuckDuckGoSearchResults
    from langchain_community.tools import WikipediaQueryRun
    from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
    from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

    ddg_wrapper = DuckDuckGoSearchAPIWrapper(region="us-en", max_results=3)
    ddg_search = DuckDuckGoSearchResults(api_wrapper=ddg_wrapper)

    wiki_wrapper = WikipediaAPIWrapper(top_k_results=3)
    wiki_search = WikipediaQueryRun(api_wrapper=wiki_wrapper)

    toolkit = [ddg_search, wiki_search]

    return toolkit


def get_github_toolkit():
    from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
    from langchain_community.utilities.github import GitHubAPIWrapper
    from dotenv import load_dotenv

    load_dotenv()

    github_wrapper = GitHubAPIWrapper()
    github = GitHubToolkit.from_github_api_wrapper(github_wrapper)
    toolkit = github.get_tools()

    return toolkit
