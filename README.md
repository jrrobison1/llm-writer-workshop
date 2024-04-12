# LLM Writer Workshop

[![CI](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/backend.yml/badge.svg)](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/backend.yml) [![CI](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/frontend.yml/badge.svg)](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/frontend.yml)

## Description

LLM Writer Workshop is a Python project that simulates a writing workshop with different roles such as agents, editors, writers, and publishers. It uses various AI models for different roles, including OpenAI's GPT-3.5 Turbo, Gemini, and Mistral.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the project dependencies, first install Poetry, then run:

```sh
poetry install
```

You also need to set up your environment variables. Copy the [``.env.example``](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjason%2FProjects%2Ftemp%2Fllm-multi-model-workshop%2F.env.example%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/jason/Projects/temp/llm-multi-model-workshop/.env.example") file to a new file named [``.env``](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjason%2FProjects%2Ftemp%2Fllm-multi-model-workshop%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/jason/Projects/temp/llm-multi-model-workshop/.env") and replace the placeholders with your actual API keys:

```sh
cp .env.example .env
```

## Usage
```sh
poetry run python app.py
```


## Testing

This project uses pytest for testing. To run the tests, use the following command:

```sh
poetry run pytest
```

## License

This project is licensed under the terms of the MIT license.

## Contact

If you have any questions, feel free to reach out to me.
