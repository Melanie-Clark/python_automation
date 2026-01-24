import xml.etree.ElementTree as ET

file_path = "practice_files/parse_data/groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

items_over_7 = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    
    if float(price) > 7.00:
      items_over_7.append(name)

    # print(name, price)
print("Items costing more than 6.00: ", items_over_7)
