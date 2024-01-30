import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_ai_response(messages: List[Dict[str, str]], model= 'gpt-3.5-turbo', temperature=0.5) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=256
    )
    # print(response)
    return response.choices[0].text
