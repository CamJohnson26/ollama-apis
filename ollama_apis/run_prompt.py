import os

from dotenv import load_dotenv
from ollama import Client

load_dotenv()

client = Client(
  host=os.environ.get("OLLAMA_API_ENDPOINT"),
)


def chat(prompt):
    response = client.chat(model='llama3.1', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
    print(response.message.content)
