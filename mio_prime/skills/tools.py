import requests
from .. import config

class ToolBox:
    def __init__(self):
        pass

    def get_weather(self, city):
        """Fetches weather from Weatherstack."""
        if not config.WEATHERSTACK_API_KEY:
            return "Weather API key missing."
        
        url = f"http://api.weatherstack.com/current?access_key={config.WEATHERSTACK_API_KEY}&query={city}"
        try:
            response = requests.get(url).json()
            if "current" in response:
                temp = response["current"]["temperature"]
                desc = response["current"]["weather_descriptions"][0]
                return f"It is currently {temp}°C and {desc} in {city}."
            else:
                return "Could not fetch weather data."
        except Exception as e:
            return f"Weather Error: {e}"

    def google_search(self, query):
        """Searches Google via SerpApi."""
        if not config.SERPAPI_API_KEY:
            return "SerpApi key missing."
        
        url = f"https://serpapi.com/search.json?q={query}&api_key={config.SERPAPI_API_KEY}"
        try:
            response = requests.get(url).json()
            if "organic_results" in response:
                top_result = response["organic_results"][0]
                snippet = top_result.get("snippet", "No snippet.")
                link = top_result.get("link", "")
                return f"Found this: {snippet} ({link})"
            elif "answer_box" in response:
                 return response["answer_box"].get("snippet", "Found an answer box but no text.")
            else:
                return "No good search results found."
        except Exception as e:
            return f"Search Error: {e}"

    def convert_currency(self, amount, from_currency, to_currency):
        """Converts currency via ExchangeRate-API."""
        if not config.EXCHANGERATE_API_KEY:
            return "ExchangeRate API key missing."
            
        url = f"https://v6.exchangerate-api.com/v6/{config.EXCHANGERATE_API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        try:
            response = requests.get(url).json()
            if response["result"] == "success":
                result = response["conversion_result"]
                return f"{amount} {from_currency} is {result} {to_currency}."
            else:
                return "Currency conversion failed."
        except Exception as e:
            return f"Currency Error: {e}"
