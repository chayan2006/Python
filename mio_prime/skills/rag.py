import os
import google.generativeai as genai
from duckduckgo_search import DDGS
from .. import config

class RAGSystem:
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None

    def search_web(self, query):
        """
        Searches DuckDuckGo for the query and returns a summary string.
        """
        print(f"[RAG] Searching web for: {query}...")
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=3))
                if not results:
                    return None
                
                context = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
                return context
        except Exception as e:
            print(f"[RAG] Search error: {e}")
            return None

    def generate_answer(self, query):
        """
        Performs RAG: Search -> Context -> LLM Answer.
        """
        if not self.model:
            return "I need a GEMINI_API_KEY in config.py to answer complex questions."

        context = self.search_web(query)
        if not context:
            return "I couldn't find any information on the web about that."

        prompt = f"""
        You are MIO PRIME, an intelligent assistant.
        Answer the following question based ONLY on the provided context.
        If the context doesn't contain the answer, say "I couldn't find that info."
        
        Context:
        {context}
        
        Question: {query}
        
        Answer:
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"I encountered an error generating the answer: {e}"
