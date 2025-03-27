"""
Main application module.
"""
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

from src.utils.logger import get_logger

# Load environment variables from .env file
load_dotenv()

# Get environment
ENV = os.getenv("ENV", "development")

# Initialize logger
logger = get_logger("main")


def main():
    """
    Main entry point for the application.
    """
    logger.info(f"Application started in {ENV} mode")

    # Load a chat model
    # ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them
    # Model information available at: https://ollama.com/VitoF/llama-3.1-8b-italian
    model = init_chat_model(
        "VitoF/llama-3.1-8b-italian:latest", model_provider="ollama"
    )
    # Note that ChatModels receive message objects as input and generate message objects as output.
    # In addition to text content, message objects convey conversational roles and hold important data, such as tool calls and token usage counts
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage(
            "hi! ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them"
        ),
    ]
    logger.info(f"Messages: {messages}")
    # Invoke the chat model
    response_message = model.invoke(messages)
    logger.info(f"Response: {response_message.content}")

    # Consider that LangChain supports also chat model input as strings:
    # The following are equivalent:
    # - model.invoke([{"role": "user", "content": "Hello"}])
    # - model.invoke([HumanMessage(content="Hello")])


if __name__ == "__main__":
    main()
