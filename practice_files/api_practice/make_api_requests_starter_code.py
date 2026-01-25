import requests

# define base URL
base_url = "https://api.upcitemdb.com/prod/trial/lookup?"

# define parameters
parameters = {"upc": "615872592913"}

# make API request, passing in base URL and parameters
response = requests.get(base_url, params=parameters)

# print out the response URL 
print(response.url)
