"""
Main application module.
"""
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

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
    # Build a prompt template
    system_template = """
    Translate the following from English into {language}.

    """
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text_to_translate}")]
    )

    # Build the actual prompt from the template
    # It returns a ChatPromptValue that consists of two messages.
    # To access the messages directly we do `prompt.to_messages()`
    prompt = prompt_template.invoke(
        {
            "language": "Italian",
            "text_to_translate": "hi! ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them",
        }
    )
    logger.info(f"Prompt: {prompt}")

    # Invoke the chat model
    response_message = model.invoke(prompt)
    logger.info(f"Response: {response_message.content}")


if __name__ == "__main__":
    main()
