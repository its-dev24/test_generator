from openai import OpenAI
from config import settings


def create_client():
    client = OpenAI(
        api_key=settings.OPENROUTER_KEY, base_url="https://openrouter.ai/api/v1/"
    )
    return client


def call_llm(prompt: str):
    client = create_client()
    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    content = response.choices[0].message.content
    return content
