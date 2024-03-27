from llm_multi_model_workshop.chatter.mistral_chatter import MistralChatter
from llm_multi_model_workshop.chatter.gemini_chatter import GeminiChatter
from llm_multi_model_workshop.chatter.openai_chatter import OpenAIChatter
from . import config_service


arthur_chatter = OpenAIChatter(
    model="gpt-3.5-turbo",
    system_prompt=config_service.get_writer_config()["persona"],
    name="Arthur",
    max_output_tokens=512,
)
luis_chatter = MistralChatter(
    model="mistral-large-latest",
    system_prompt=config_service.get_editor_config()["persona"],
    name="Luis",
    max_output_tokens=512,
)
heidi_chatter = GeminiChatter(
    model="gemini-pro",
    system_prompt=config_service.get_agent_config()["persona"],
    name="Heidi",
    max_output_tokens=512,
)
yolanda_chatter = OpenAIChatter(
    model="gpt-4",
    system_prompt=config_service.get_publisher_config()["persona"],
    name="Yolanda",
    max_output_tokens=1024,
)

# Give the writing sample to the personas
# luis_chatter.add_to_history(question)
# luis_response = (
#     "Here is what Luis thinks about the original writing: \n***\n"
#     + luis_chatter.chat("")
#     + "\n***\n"
# )

# heidi_chatter.add_to_history(luis_response)
# heidi_chatter.add_to_history(question)
# heidi_response = (
#     "Here is what Heidi thinks about the original writing: \n***\n"
#     + heidi_chatter.chat("")
#     + "\n***\n"
# )

# arthur_chatter.add_to_history(luis_response)
# arthur_chatter.add_to_history(heidi_response)
# arthur_chatter.add_to_history(question)
# arthur_response = (
#     "Here is what Arthur thinks about the original writing: \n***\n"
#     + arthur_chatter.chat("")
#     + "\n***\n"
# )

# response = yolanda_chatter.chat(question)


def chat(text):
    request = (
        "Here is the original writing for critique, written by User: \n***"
        + text
        + "\n***\n"
    )
    feedbacks = luis_chatter.chat(request)
    return feedbacks
