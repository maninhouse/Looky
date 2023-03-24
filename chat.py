import os
import openai as ai
from dotenv import load_dotenv

load_dotenv()

ai.api_key = os.getenv("OPENAI_API_KEY")

def ask(question: str) -> str:
    response = ai.Completion.create(
    model="text-davinci-003",
    prompt=f"Human: {question}\nAI:",
    temperature=0.9,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    # print(response)
    return response.choices[0].text
