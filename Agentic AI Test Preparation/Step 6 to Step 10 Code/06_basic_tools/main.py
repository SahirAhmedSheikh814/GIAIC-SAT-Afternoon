from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import asyncio


# Get environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_base_url = os.getenv("GEMINI_BASE_URL")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
if not gemini_api_base_url:
    raise ValueError("GEMINI_BASE_URL environment variable is not set")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = gemini_api_base_url,
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

