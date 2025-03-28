# LangChain Chat Translator

This project showcases a powerful English-to-Italian translation application built with LangChain and Ollama. It leverages the capabilities of the `llama-3.1-8b-italian` model to provide accurate and contextually appropriate translations.
It has been developed as an extension of the [LangChain tutorial](https://python.langchain.com/docs/tutorials/llm_chain/), this application demonstrates how to effectively implement LLM-powered language processing within a structured application framework.

## Key Features

- Integration with LangChain for structured LLM interactions
- Uses Ollama as a local model provider
- Translation from English to Italian using LLaMa 3.1 (8B parameter Italian model)
- Comprehensive logging system
- Environment variable management

## Project Structure

```
project_root/
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
├── src/                  # Source code directory
│   ├── __init__.py
│   ├── main.py           # Main application file
│   └── utils/            # Utility modules
│       ├── __init__.py
│       └── logger.py     # Logging configuration
├── tests/                # Test directory
│   └── __init__.py
└── logs/                 # Directory for log files
```

## Setup

### Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (MacOS/Linux)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate
```

### Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

### Environment Variables

Configure your environment variables in the `.env` file.

## Usage

### Prerequisites

1. Make sure you have [Ollama](https://ollama.ai/) installed and running locally.
2. Pull the required model:
   ```bash
   ollama pull VitoF/llama-3.1-8b-italian:latest
   ```

### Running the Application

Run the main application:

```bash
python -m src.main
```

This will:
1. Initialize the LangChain chat model with the Italian LLaMa model
2. Send a predefined English text for translation
3. Log the response to the console and log files

### Customizing Translations

To translate your own text, modify the `HumanMessage` content in `src/main.py`:

```python
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage(content="Your English text here")
]
```

### Sample Output

When running the application, you'll see output similar to:

```
2025-03-27 14:52:20.123 | INFO     | main:main:30 - Application started in development mode
2025-03-27 14:52:21.456 | INFO     | main:main:41 - Messages: [SystemMessage(content='Translate the following from English into Italian'), HumanMessage(content='hi! ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them')]
2025-03-27 14:52:25.789 | INFO     | main:main:44 - Response: Ciao! I ChatModels sono istanze di LangChain Runnables, il che significa che espongono un'interfaccia standard per interagire con essi
```

## Running Tests

Run tests using pytest:

```bash
pytest
```

## Code Quality Tools

This project uses several tools to maintain code quality:

### Pre-commit Hooks

Pre-commit hooks automatically check your code before each commit to ensure it meets quality standards. The hooks run:

- **isort**: Sorts and formats imports
- **black**: Formats code to a consistent style
- Additional checks for trailing whitespace, file endings, etc.

To set up pre-commit hooks:

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```

Once installed, the hooks will run automatically on every commit. You can also run them manually:

```bash
# Run on all files
pre-commit run --all-files

# Run a specific hook
pre-commit run black
```

If a hook fails, the commit will be aborted. Fix the issues and try committing again.
