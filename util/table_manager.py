import json

def add_inventory_item():
    # Add a new item to the inventory table
    item = {
        "name": input("Enter item name: "),
        "cost_price": float(input("Enter cost price: ")),
        "selling_price": float(input("Enter selling price: ")),
        "quantity": int(input("Enter quantity: ")),
        "category": input("Enter category: ")
    }
    with open('data/inventory.json', 'r+') as file:
        data = json.load(file)
        data['items'].append(item)
        file.seek(0)
        json.dump(data, file, indent=4)

