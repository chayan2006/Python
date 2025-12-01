import os
from groq import Groq

# Hardcoded key from user request to be sure
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

try:
    print(f"Testing Groq API with key: {API_KEY[:10]}...")
    client = Groq(api_key=API_KEY)
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hello",
            }
        ],
        model="llama3-8b-8192",
    )
    print("Success!")
    print(chat_completion.choices[0].message.content)

except Exception as e:
    print("FAILED")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
