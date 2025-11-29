from . import config, auth, memory, learning
from .skills import device, rag, jarvis_brain, tools

class MioAgent:
    def __init__(self):
        self.auth = auth.Authenticator()
        self.memory = memory.ShortTermMemory()
        self.logger = memory.Logger()
        self.device_skills = device.DeviceSkills()
        self.knowledge_base = learning.KnowledgeBase()
        self.rag_system = rag.RAGSystem()
        self.jarvis = jarvis_brain.JarvisBrain()
        self.tools = tools.ToolBox()
        
        # BYPASS AUTHENTICATION (User Request)
        self.is_authenticated = True 
        self.last_query = None
        self.last_response = None

    def start_session(self):
        print(f"SYSTEM MESSAGE — {config.SYSTEM_NAME}")
        print(f"Welcome, Owner {config.OWNER_NAME}.")
        print("MIO is online and awaiting commands.")

    def process_command(self, command):
        if not self.is_authenticated:
            print("Access denied. Please authenticate first.")
            return

        self.logger.log("COMMAND", "RECEIVED", command)
        
        response = ""
        cmd_lower = command.lower()

        # --- COMMAND DISPATCHING ---

        # 1. System Commands
        if "halt" in cmd_lower:
            print("Mio, halting now.")
            self.logger.log("SYSTEM", "HALT", "User requested halt")
            return "HALT"
        
        # 2. Device Control
        elif "open" in cmd_lower:
            app_name = cmd_lower.replace("open", "").strip()
            if app_name:
                success = self.device_skills.open_app(app_name)
                response = f"Opening {app_name}..." if success else f"Could not open {app_name}."
            else:
                response = "What should I open?"

        # 3. Identity
        elif "who are you" in cmd_lower:
            response = f"I am {config.SYSTEM_NAME}, owner-bound to {config.OWNER_NAME}."

        # 4. Tools (Regex/Keyword matching for speed)
        elif "weather" in cmd_lower:
            # Extract city (naive)
            words = command.split()
            city = words[-1] # Assume last word is city for now, or prompts
            if "in" in words:
                city = command.split("in")[-1].strip()
            response = self.tools.get_weather(city)
            
        elif "convert" in cmd_lower and "to" in cmd_lower:
            # naive parsing: convert 100 USD to EUR
            try:
                parts = command.split()
                amount = parts[1]
                from_curr = parts[2].upper()
                to_curr = parts[4].upper()
                response = self.tools.convert_currency(amount, from_curr, to_curr)
            except:
                response = "I didn't understand the currency format. Try: 'Convert 100 USD to EUR'."

        elif "search" in cmd_lower or "google" in cmd_lower:
            query = command.replace("search", "").replace("google", "").strip()
            response = self.tools.google_search(query)

        # 5. Knowledge Base (User taught)
        elif self.knowledge_base.get_response(command):
             response = self.knowledge_base.get_response(command)

        # 6. Jarvis Brain (Groq) - The default conversationalist
        else:
            # Use Groq for everything else (General knowledge, chat, complex queries)
            
            # Get short-term memory context
            history = self.memory.get_context()
            
            response = self.jarvis.chat(command, history=history)

        print(f"MIO: {response}")
        self.memory.add_interaction(command, response)
        self.logger.log("COMMAND", "EXECUTED", response)
        
        # Store context for potential feedback
        self.last_query = command
        self.last_response = response
        
        return "CONTINUE"
