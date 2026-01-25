import requests
from api_key import API_KEY

# define base URL
base_url = "http://api.openweathermap.org/data/2.5/forecast"

"""
Create a new file api_practice/api_key.py
Assign your api key to the variable API_KEY
"""

# define parameters
parameters = {"q": "Paris,FR", "appid": API_KEY}

# make API request, passing in base URL and parameters
response = requests.get(base_url, params = parameters)

# print out text from API response
print(response.text)
