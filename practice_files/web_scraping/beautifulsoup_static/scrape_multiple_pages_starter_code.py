import requests 

# BeautifulSoup is for static HTML 
from bs4 import BeautifulSoup
from time import sleep

# for loop to iterate over the range of page numbers you want to scrape from
for page_number in range(1,6):

  url = "https://www.petsathome.com/campaigns/listing/dog-treats-offers?page="+str(page_number)

  # send a request to get html code from that url
  response = requests.get(url, headers={"Accept": "text/html"}) 

  # parse the response
  parsed_response = BeautifulSoup(response.text, "html.parser") 

  # extract ALL the dog treat names from that page
  dog_treat_elements = parsed_response.find_all("h3", class_="product-info_title__2XVM2 type-w-bold")

  # extract ALL the prices specific to the dog treats from that page
  dog_treat_price_elements = parsed_response.find_all("p", class_="product-price_price__ukg_k")

  # print out the page number 
  print("\nPage Number:", page_number)

  # print out the dog treat names on the page after formatting the text 
  """
  map() applies the function to every item in the list
  For each element x, it gets the text and strips whitespace
  """
  print("\nDog Treat:", list(map(lambda x: x.text.strip(), dog_treat_elements)))

  # print out the book authors appearing on that page after formatting the text 
  print("\nPrice:", list(map(lambda x: x.text.strip(), dog_treat_price_elements)))

  # pause the program for 1 second between iterations of the loop
  sleep(1)
