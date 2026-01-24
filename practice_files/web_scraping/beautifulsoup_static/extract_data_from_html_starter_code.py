import requests 
from bs4 import BeautifulSoup 

url = "https://www.petsathome.com/campaigns/listing/dog-treats-offers"

# send a request to get html code from the url and save the response 
response = requests.get(url, headers={"Accept": "text/html"}) 

# use BeautifulSoup to parse the text from the response 
parsed_response = BeautifulSoup(response.text, "html.parser") 

# find all dog treats
dog_treats = parsed_response.find_all("h3", class_="product-info_title__2XVM2 type-w-bold")

# iterate over the titles and print the text for each
for treat_name in dog_treats:
    print(treat_name.text)
