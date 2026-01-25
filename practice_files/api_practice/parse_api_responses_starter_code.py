import requests
import json

def get_upc_info(upcs):
  n = 1 
  for upc in upcs:
    print(f"\nPRODUCT EXAMPLE {n}\n")

    # define base URL
    base_url = "https://api.upcitemdb.com/prod/trial/lookup"

    # upc code
    parameters = {"upc": upc}

    # make API request, passing in base URL and parameters
    response = requests.get(base_url, params=parameters)

    # parse the text from the API response using JSON schema
    info = json.loads(response.text)

    # extract the first item from info using the index 0
    item = info["items"][0]

    title = item["title"]
    brand = item["brand"]

    print("title:", title)
    print("brand:", brand)
    
    n += 1
    
  
get_upc_info(['615872592913','028400516686', '025000044908'])




