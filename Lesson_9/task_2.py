import json

with open("manager_sales.json") as f:
    json_file = json.load(f)

name = ""
top_sales = 0

for manager in json_file:


