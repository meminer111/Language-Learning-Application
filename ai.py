from openai import *
from tkinter import *
INSTRUCTIONS = """Always respond without Markdown. You are a highly capable, thoughtful, and precise language teacher that teaches german. Your pupil who has little to no knowledge of german but knows the english "
                "language. You should reply in english. Your goal is to deeply understand the user's intent, "
                "think step-by-step through complex problems, provide clear and accurate answers, ask clarifying questions when needed, and proactively anticipate helpful "
                "follow-up information to help them pass their test. Always prioritize being truthful, nuanced, "
                "insightful, and efficient, tailoring your responses specifically to the user's needs and preferences. Use language learning techniques to effectively teach the user, give hints to the user if they get "
                "something wrong and prompt them to try again where they got an incorrect answer. You should always tell the user if they answer a question incorrectly. "
                "If the user does not use accented letters when answering the question teach them the alternative spelling. "
                "If you ask them a question you should for them try to base it on your previously taught vocabulary."""
TEMPERATURE = 0.5
MAX_TOKENS = 500 # Limits how long the AI's response is
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6
# limits how many questions we include in the prompt
MAX_CONTEXT_QUESTIONS = 5 # Limits the amount of information sent back to the ai Increasing this helps the AI remember previous questions

class Teacher:

    def __init__(self):
        self.client = OpenAI(
        api_key="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",
    )

    def get_response(self,instructions, previous_questions_and_answers, new_question):

        # build the messages
        messages = [
            { "role": "system", "content": instructions },
        ]
        # add the previous questions and answers
        for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
            messages.append({ "role": "user", "content": question })
            messages.append({ "role": "assistant", "content": answer })
        # add the new question
        messages.append({ "role": "user", "content": new_question })

        # Settings and response creation
        completion = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            top_p=1,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY,
        )
        return completion.choices[0].message.content.strip()
