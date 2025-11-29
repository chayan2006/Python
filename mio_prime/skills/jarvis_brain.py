import os
from groq import Groq
from .. import config

class JarvisBrain:
    def __init__(self):
        try:
            self.client = Groq(api_key=config.GROQ_API_KEY)
            self.model = "llama-3.1-8b-instant" # Verified working model
        except Exception as e:
            print(f"Groq Init Error: {e}")
            self.client = None

    def chat(self, user_input, history=None, system_prompt=None):
        if not self.client:
            return "My brain (Groq) is not connected."

        if not system_prompt:
            system_prompt = (
                f"You are {config.SYSTEM_NAME}, an advanced AI assistant created by {config.OWNER_NAME}. "
                "You are witty, precise, and helpful. You have access to real-time tools. "
                "Keep answers concise and human-like. Do not sound robotic."
            )

        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history
        if history:
            for interaction in history:
                # Assuming interaction is a dict {'user': '...', 'agent': '...'}
                messages.append({"role": "user", "content": interaction['user']})
                messages.append({"role": "assistant", "content": interaction['agent']})

        # Add current query
        messages.append({"role": "user", "content": user_input})

        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=0.7,
                max_tokens=1024,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Brain Error: {e}"
