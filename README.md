# LLM Writer Workshop

[![CI](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/backend.yml/badge.svg)](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/backend.yml) [![CI](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/frontend.yml/badge.svg)](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/frontend.yml) [![CI](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/docker.yml/badge.svg)](https://github.com/jrrobison1/llm-writer-workshop/actions/workflows/docker.yml)


## Description
LLM Writer Workshop simulates a creative writing workshop with different roles: a writing agent, an editor, a fellow writer, and a publisher. It uses various selectable AI models for different roles, including OpenAI's GPT-4 and GPT-3.5 Turbo; Anthropic's Claude Haiku, Sonnet, and Opus; Google's Gemini; and Mistral's small, medium, and large. The project is written with a Python/Flask backend and a TypeScript/React frontend.

I made this because I wanted AI to help me write, not write _for_ me. I wanted the virtual experience of getting feedback from multiple points of view within the same workshop session. And I wanted the ability to receive different points of view—by selecting different models—even for the same persona.

![Publisher Feedback](/.images/publisher_feedback_20240414.png "Publisher Feedback")

## Build and run with Docker
1. Clone this repository and cd into it
2. Install Docker if have not already: https://docs.docker.com/engine/install/
3. Ensure you have your API keys set (see below)

Then:
```sh
docker-compose up --build
```

Connect to http://localhost:3000 in your browser.


### API Keys
You will need API keys to run this project. Here are instructions for creating these api keys:<br />
OpenAI: https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key<br />
Claude: https://docs.anthropic.com/claude/reference/getting-started-with-the-api<br />
Gemini: https://ai.google.dev/tutorials/get_started_web<br />
Mistral: https://docs.mistral.ai/

Copy the `.env.example` in the "service" directory to a new file named `.env` in the "service" directory, and replace the placeholders with your actual API keys:

```sh
cp ./service/.env.example ./service/.env

# Or use your favorite editor here
vim ./service/.env
```

If you are building manually (see below), another option is just to set the environment variables in your environment:<br />
```sh
export OPENAI_API_KEY=<your_openai_api_key>
export ANTHROPIC_API_KEY=<your_anthropic_api_key>
export GEMINI_API_KEY=<your_gemini_api_key>
export MISTRAL_API_KEY=<your_mistral_api_key>
```


## Building manually

### Backend
#### Dependencies
This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the project dependencies, first install Poetry:
```sh
pip install poetry
```
Then run:
```sh
cd service
poetry install
```


### UI
```sh
cd ui
npm install
```




## Manually launching the app after building the frontend and the backend:
Perform the following steps, then visit http://localhost:3000 in your browser.

### Backend
```sh
cd service && poetry run python app.py
```

### Frontend
```sh
cd ui
npm start
```

## Optional Configuration
The different personas in the workshop (editor, agent, writer, and publisher) are created through system prompts, which are defined in `service/service/config/config.toml`. You may edit this file to easily use your own prompts instead of the defaults.

## Roadmap
- Streaming to UI
- Different prompts selectable through the UI
- Disable model selection based on token count of writing
- Disable model selection based on usage limitations (e.g. gemini-pro-1.5 only 2 times/minute)
- Support for local models

## License
This project is licensed under the terms of the MIT license.
