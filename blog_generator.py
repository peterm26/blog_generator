import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog(topic):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes blog paragraphs."},
            {"role": "user", "content": f"Write a paragraph about: {topic}"}
        ],
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

while input("Write a paragraph? (Y to continue): ").upper() == 'Y':
    topic = input("What should this paragraph talk about? ")
    print("\n" + generate_blog(topic) + "\n")
