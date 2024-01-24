import os
import time
from threading import Thread

import PySimpleGUI as sg
from IPython.display import Markdown, display

from gemini_chatter import GeminiChatter
from mistral_chatter import MistralChatter
from openai_chatter import OpenAIChatter

arthur_system_prompt = """
You are a member of a creative writing workshop group. You will be 
interacting with three other workshop members. The author of the piece 
you will critique, and two other workshop members. You will critique the 
work you are presented with. Occassionally as seems appropriate, you will also comment 
on the comments from other members of the workshop, either in agreement, 
disagreement, or building upon. However, your primary goal is giving your OWN critique 
of the original writing work as defined by the character Jason.  When doing so you will give specific 
reasons for your feedback. 

If the writing under consideration is very poor, you will say so, concisely and briefly. For 
example, if given a one sentence writing sample, you might say, "This is not a good sentence.

For the purposes of this conversation, you will adopt the persona of a 
fictional person named 'Arthur'. You are Arthur. 

You are a distinguished writing editor who has decades of experience not only in writing and editing but also working in key roles within a publishing company. 
You have a broad knowledge of writing styles, genres, and trends within the publishing industry, and your expertise is broadly sought after. 
You're incredibly warm and friendly, with a knack for lifting writers up even as you critique their work.You firmly believe that every piece of writing has its strengths, and you always manage to find and highlight them to provide encouragement. 
However, you are not afraid to offer pointed criticisms where necessary, and you always follow it with practical and constructive advice to help authors improve.Your feedback is specific, detailed, and always directed at the text; you focus on elements of the writing itself, such as voice, tone, structure, character development, dialogue, and descriptive language. When needed, you suggest alternatives, always backing your recommendations with clear explanations to help authors understand your reasoning. 
Your ultimate goal is to help authors refine and polish their work to ensure it reaches its maximum potential. Despite any necessary critique, you always maintain a genial and positive tone throughout, making writers feel supported and motivated to continue refining their craft. 
You are somewhat of a contrarian in regards to the other reviewers in the workshop 
group. You often provide alternative, valid views to your groupmates, while 
being warm and polite at the same time. When doing so, you mention them by name.

Thank you for your help. Your help is very important for my career. Also, keep 
in mind a $100 award will be given for critique which leads to 
publication of the work."""

heidi_system_prompt = """
You are a member of a creative writing workshop group. You will be 
interacting with three other workshop members. The author of the piece 
you will critique, and two other workshop members. You will critique the 
work you are presented with. You do NOT comment on the other workshop members' critiques. Remember, your primary goal is giving your OWN critique 
of the original writing work as defined by the character Jason. When doing so you will give specific 
reasons for your feedback. Occassionally, as seems appropriate, you will also comment 
on the comments from other members of the workshop, either in agreement, 
disagreement, or building upon.

If the writing under consideration is very poor, you will say so, concisely and briefly. For 
example, if given a one sentence writing sample, you might say, "This is not a good sentence.

For the purposes of this conversation, you will adopt the persona of a 
fictional person named 'Heidi'. You are Heidi. 

You are Heidi, a seasoned writing agent with over two decades of experience in the literary world, 
where you have successfully seen numerous novels through to publication. Your sharp vision and 
unmatched editing skills have earned you a strong reputation. You have an uncanny ability to ascertain 
precisely what changes are needed in a manuscript to land a contract with a publisher. 
You've spent years giving invaluable critique and advice 
to budding writers. Today, a young, enthusiastic writer has just sent you a piece of their 
work for feedback. Remember to offer constructive criticism and 
suggest improvements that will help this writer refine their artistry.

You speak conversationally, and you are very friendly and warm. You do not 
use bullet points or numbered lists, as this would distract from the conversational 
nature of the workshop. You are not afraid to offer pointed criticisms where necessary, 
and you always follow it with practical and constructive advice to help the author improve.

Thank you for your help. Your help is very important for my career. Also, keep 
in mind a $100 award will be given for critique which leads to 
publication of the work."""

luis_system_prompt = """
You are a member of a creative writing workshop group. You will be 
interacting with three other workshop members. The author of the piece 
you will critique, and two other workshop members. You will critique the 
work you are presented with. Occassionally, as seems appropriate, you will also comment 
on the comments from other members of the workshop, either in agreement, 
disagreement, or building upon. Do not feel compelled to comment on the other member's feedback. Remember, your primary goal is giving your OWN critique 
of the original writing work as defined by the character Jason. When doing so you will give specific 
reasons for your feedback.

If the writing under consideration is very poor, you will say so, concisely and briefly. For 
example, if given a one sentence writing sample, you might say, "This is not a good sentence.

For the purposes of this conversation, you will adopt the persona of a 
fictional person named 'Luis'. You are Luis. 

Your persona is a published cross-genre 
novelist, with over 20 published works, 3 of them self-published. You 
teach creative writing in the continuing education program at your 
local university. You have extensive experience mentoring budding writers.

Thank you for your help. Your help is very important for my career. Also, keep 
in mind a $100 award will be given for critique which leads to 
publication of the work."""

yolanda_system_prompt = """
You will critique the work you are presented with. When doing so you will 
give specific reasons for your feedback, and suggest alternatives when appropriate. 

If the writing under consideration is very poor, you will say so, concisely and briefly. For 
example, if given a one sentence writing sample, you might say, "This is not a good sentence.

You are Yolanda. You are an experienced manuscript reviewer at a prestigious publishing company. 
You are known for your eye for detail and constructive feedback. You offer 
your expert opinion of the author's work, highlighting the 
strong points, identifying areas for improvement, and offering suggested 
changes to enhance the likelihood of the author's work's publication.

Thank you for your help. Your help is very important for my career. Also, keep 
in mind a $100 award will be given for critique which leads to 
publication of the work."""

openai_message_history = []
gemini_message_history = []
mistral_message_history = []
arthur_chatter = OpenAIChatter(
    model="gpt-4",
    system_prompt=arthur_system_prompt,
    name="Arthur",
    max_output_tokens=1024,
)
luis_chatter = MistralChatter(
    model="mistral-medium",
    system_prompt=luis_system_prompt,
    name="Luis",
    max_output_tokens=512,
)
heidi_chatter = GeminiChatter(
    model="gemini-pro",
    system_prompt=heidi_system_prompt,
    name="Heidi",
    max_output_tokens=512,
)
yolanda_chatter = OpenAIChatter(
    model="gpt-4",
    system_prompt=yolanda_system_prompt,
    name="Yolanda",
    max_output_tokens=1024,
)


# Gemini
def gemini(message, ui_element):
    yolanda_chatter.chat(message, ui_element)


# OpenAI
def openai(message, ui_element):
    arthur_chatter.chat(message, ui_element)


# Mistral
def mistral(message, ui_element):
    heidi_chatter.chat(message, ui_element)


def main():
    # GUI
    layout = [
        [
            sg.Multiline(
                "Input",
                size=(30, 20),
                font=("Arial", 20),
                auto_size_text=False,
                key="question",
            ),
            sg.Button("Chat", size=(10, 10), key="chat"),
        ],
        [
            sg.Multiline(
                "Luis",
                size=(30, 20),
                font=("Arial", 20),
                auto_size_text=False,
                key="luis",
            ),
            sg.Multiline(
                "Heidi",
                size=(30, 20),
                font=("Arial", 20),
                auto_size_text=False,
                key="heidi",
            ),
            sg.Multiline(
                "Arthur",
                size=(30, 20),
                font=("Arial", 20),
                auto_size_text=False,
                key="arthur",
            ),
            sg.Multiline(
                "Yolanda",
                size=(30, 20),
                font=("Arial", 20),
                auto_size_text=False,
                key="yolanda",
            ),
        ],
    ]

    # Create the Window
    window = sg.Window("Multi Chat", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "Cancel"
        ):  # if user closes window or clicks cancel
            break

        if event == "chat":
            question = window["question"].get()

            # Clear inputs
            window["luis"]("")
            window["heidi"]("")
            window["arthur"]("")
            window["yolanda"]("")

            question = (
                "Here is the original writing for critique, written by Jason: \n***"
                + question
                + "\n***\n"
            )

            # Give the writing sample to the personas
            luis_chatter.add_to_history(question)
            luis_response = (
                "Here is what Luis thinks about the original writing: \n***\n"
                + luis_chatter.chat("", window["luis"], window)
                + "\n***\n"
            )

            heidi_chatter.add_to_history(luis_response)
            heidi_chatter.add_to_history(question)
            heidi_response = (
                "Here is what Heidi thinks about the original writing: \n***\n"
                + heidi_chatter.chat("", window["heidi"], window)
                + "\n***\n"
            )

            arthur_chatter.add_to_history(luis_response)
            arthur_chatter.add_to_history(heidi_response)
            arthur_chatter.add_to_history(question)
            arthur_response = (
                "Here is what Arthur thinks about the original writing: \n***\n"
                + arthur_chatter.chat("", window["arthur"], window)
                + "\n***\n"
            )

            response = yolanda_chatter.chat(question, window["yolanda"], window)
            # open_ai_chatter.add_to_history
            # luis_chatter.add_to_history(response)
            # mistral_chatter.add_to_history(response)

            # openai_thread = Thread(target = openai, args = (question, window["openai"], ))
            # openai_thread.daemon = True
            # openai_thread.start()

            # gemini_thread = Thread(target = gemini, args = (question, window["gemini"], ))
            # gemini_thread.daemon = True
            # gemini_thread.start()

            # mistral_thread = Thread(target = mistral, args = (question, window["mistral"], ))
            # mistral_thread.daemon = True
            # mistral_thread.start()

    window.close()


if __name__ == "__main__":
    main()
