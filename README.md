# Python Project

This is a Python project scaffold with basic configuration for development.

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

Run the main application:

```bash
python -m src.main
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
- **flake8**: Checks for code issues and style problems
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
