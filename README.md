# llm-multi-model-writer-workshop
Workshop your writing with AI teammates. Workshop members can be any of Gemini, OpenAI, or Mistral. Members may comment on each other's criticism.

<img width="1564" alt="gui_screenshot" src="https://github.com/jrrobison1/llm-multi-model-writer-workshop/assets/157397847/407da68a-7b20-4ad5-a77d-bdf592d2457f">

## Requirements
_Note: This program requires real API keys. You will be charged for your usage by your API provider
- API keys. You must have an API key for each model type you would like to use
- Environment variables. The program expects the following:
   - OPENAI_API_KEY
   - GEMINI_API_KEY
   - MISTRAL_API_KEY
 
## Installation
1. Clone the repository
2. Within the project directory, run
   - `python -m venv virtualenv/`
   - `python -m pip install -r requirements.txt`

## Usage
Input your writing in the box on the top left and hit the "Chat" button. Wait to get the valuable feedback of your AI teammates.

## Road Map
- Persona creation to separate external files instead of hard-coded
- Checkboxes to allow user-selectable models
- UI overhaul
- Code cleanup
