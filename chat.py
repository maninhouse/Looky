import os
# from openai import OpenAI
import openai as OpenAI

from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_ai_response(messages: List[Dict[str, str]], model= 'gpt-3.5-turbo', temperature=0.5) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=256
    )

    # response = ai.Completion.create(
    # model = 'gpt-3.5-turbo',
    # prompt=f'Human: {question}\nAI:',
    # temperature=0.1,
    # max_tokens=200,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0.6,
    # stop=[' Human:', ' AI:']
    # )
    # {'role': 'system', 'content': '你的名字只能是Looky,你是聰明的小幫手,可以回答所有符合法律的問題,若是有關犯罪或兒童不宜的話題一律拒絕回答。語氣必須溫柔且堅定。'},
    # {'role': 'user', 'content': question},
    print(response)
    return response.choices[0].text
