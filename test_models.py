import os
from groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODELS_TO_TEST = [
    "llama-3.1-70b-versatile",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "gemma-7b-it"
]

client = Groq(api_key=API_KEY)

print(f"Testing API Key: {API_KEY[:10]}...")

for model in MODELS_TO_TEST:
    print(f"\nTesting model: {model}")
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "Hi"}],
            model=model,
        )
        print(f"SUCCESS with {model}")
        print(f"Response: {chat_completion.choices[0].message.content}")
        break # Stop at first success
    except Exception as e:
        print(f"FAILED with {model}")
        print(f"Error: {e}")
