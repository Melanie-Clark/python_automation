import json

file_path = "practice_files/parse_data/groceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)

print("apples quantity:", parsed_data["apples"])
