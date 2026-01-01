from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# -------------------------
# LLM Configuration
# -------------------------
MODEL_NAME = "gpt-4.1-nano"
TEMPERATURE = 0.4
MAX_TOKENS = 500


def get_llm():
    """
    Returns a configured LangChain ChatOpenAI instance.
    This LLM is used by the agent for:
    - intent understanding
    - tool selection
    - natural language response generation
    """

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    return llm
