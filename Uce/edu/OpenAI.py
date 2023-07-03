import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ' '


def inference(prompt: str) -> list:
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres una calculadora factorial solo acepta números no palabras"},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    print("TERMINATE")
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]
