from fastapi import FastAPI
import uvicorn

from llm_agent.v1.endpoints import router as v1_router

app = FastAPI(title="LLM Agent API")

app.include_router(router=v1_router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    