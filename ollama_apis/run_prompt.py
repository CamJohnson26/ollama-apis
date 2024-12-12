from ollama import Client

client = Client(
  host='http://192.168.50.140:11434',
)


def chat(prompt):
    response = client.chat(model='llama3.1', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
    print(response.message.content)
