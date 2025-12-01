import os

# System Configuration
OWNER_NAME = "Chayan Khatua"
SYSTEM_NAME = "MIO PRIME v1.2"
VERSION = "1.2.0"

# Security
SECRET_PHRASE = "Mio, proceed." # Fallback if voice key missing
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")
WEATHERSTACK_API_KEY = os.environ.get("WEATHERSTACK_API_KEY")
EXCHANGERATE_API_KEY = os.environ.get("EXCHANGERATE_API_KEY")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_DIR = os.path.join(BASE_DIR, 'memory')
LOG_FILE = os.path.join(MEMORY_DIR, 'activity.log')
KNOWLEDGE_FILE = os.path.join(MEMORY_DIR, 'knowledge.json')
VOICE_KEY_FILE = os.path.join(MEMORY_DIR, 'voice_key.txt')

# Create directories if they don't exist
os.makedirs(MEMORY_DIR, exist_ok=True)
