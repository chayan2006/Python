import json
import os
from . import config
from difflib import get_close_matches

class KnowledgeBase:
    def __init__(self):
        self.file_path = os.path.join(config.MEMORY_DIR, "knowledge.json")
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def get_response(self, query):
        """
        Returns the response for a query if it exists.
        Uses exact match for now, but could use fuzzy matching.
        """
        query = query.lower().strip()
        
        # Exact match
        if query in self.data:
            return self.data[query]
            
        # Fuzzy match (simple)
        matches = get_close_matches(query, self.data.keys(), n=1, cutoff=0.8)
        if matches:
            return self.data[matches[0]]
            
        return None

    def learn(self, query, response):
        """
        Adds a new query-response pair to the knowledge base.
        """
        query = query.lower().strip()
        self.data[query] = response
        self._save()
