import requests
from bs4 import BeautifulSoup

url = "https://www.agilityplaza.com/agilityClass/1478531665/results"

# send a GET request to get html code from that url
# The Accept header specifies that we want an HTML response
response = requests.get(url, headers={"Accept": "text/html"})
# print(response) # [200]
# print("=============================")

# parse the HTML response
parsed_response = BeautifulSoup(response.text, "html.parser")

# format the parsed HTML response in a way that’s easier to read and print it out
print(parsed_response.prettify())
