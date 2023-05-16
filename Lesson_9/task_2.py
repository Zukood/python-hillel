import json

with open('manager_sales.json') as file:
    data = json.load(file)

max_sales = 0
best_manager = ""

for record in data:
    manager = record["manager"]
    sales = sum(car["price"] for car in record["cars"])

    if sales > max_sales:
        max_sales = sales
        best_manager = manager

result = f"{best_manager['first_name']} {best_manager['last_name']}: {max_sales}"
print(result)
