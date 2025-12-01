import os
from groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
model = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)
print(f"Testing {model}...")
try:
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hi"}],
        model=model,
    )
    print("SUCCESS")
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print("FAILED")
    print(e)
