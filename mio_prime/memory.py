import os
import datetime
import json
from . import config

class Logger:
    def __init__(self):
        self.log_file = config.LOG_FILE

    def log(self, action, status, details=""):
        timestamp = datetime.datetime.now().isoformat()
        entry = f"[{timestamp}] [{action}] [{status}] {details}\n"
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)
            
    def log_security_event(self, event_type, details):
        self.log("SECURITY", event_type, details)

class ShortTermMemory:
    def __init__(self):
        self.context = []

    def add_interaction(self, user_input, agent_response):
        self.context.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "user": user_input,
            "agent": agent_response
        })
        # Keep only last 10 interactions
        if len(self.context) > 10:
            self.context.pop(0)

    def get_context(self):
        return self.context
