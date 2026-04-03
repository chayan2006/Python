# 🌐 Connecting to the Web: APIs and HTTP Requests

import requests # External module (most popular in the world!)
# How to install: pip install requests 

import json

# 1. The GET Request: Fetching Data from an API
# Example: Using a public REST API (GitHub's)
url = "https://api.github.com/users/chayan2006"

response = requests.get(url)

if response.status_code == 200:
    print("Request Successful!")
    # response.json() automatically converts JSON string to Python dictionary
    data = response.json()
    print(f"User: {data['name']}, Followers: {data['followers']}")
else:
    print(f"Request failed with status code: {response.status_code}")

# 2. Sending Data (POST Request)
# Usually used for creating new resources
# (This URL is a placeholder to show how it's done)
post_url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learning Python",
    "body": "I am mastering the web!",
    "userId": 1
}

# Sending the dictionary as JSON data
post_response = requests.post(post_url, json=payload)
print("POST Result:", post_response.status_code)
# Returns 201 Created

# 3. Parameters in URL
# Example: Searching for repos
params = {"q": "python-learning", "sort": "stars"}
search_response = requests.get("https://api.github.com/search/repositories", params=params)

# 4. Working with Headers (Authentication, type, etc.)
headers = {
    "User-Agent": "MyAwesomeApp/1.0",
    "Accept": "application/json"
}
# requests.get(url, headers=headers)

# Summary of HTTP Status Codes
"""
| Status Code | Meaning                      |
|-------------|------------------------------|
| 200 OK      | Success!                     |
| 201 Created | Resource created (POST/PUT) |
| 400 Bad     | Client error (bad request)   |
| 401 Unauth  | Missing credentials          |
| 404 No      | Not found                    |
| 500 Server  | Something broke on server    |
| 503 Service | Server is down (maintenance) |
"""
