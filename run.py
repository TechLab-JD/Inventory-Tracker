import pandas as pd
import json
import os

inventory = []

def create_inventory_file():
    # Create an empty inventory JSON file if it doesn't exist
    with open('data/inventory.json', 'w') as file:
        json.dump({}, file)
    # Add default data to the inventory file
    json_default_data = {"items": [
        {
            "name": "Sample Item",
            "cost_price": 10.0,
            "selling_price": 15.0,
            "quantity": 100,
            "category": "Sample Category"
        }
    ]}
    with open('data/inventory.json', 'w') as file:
        json.dump(json_default_data, file, indent=4)

def inventory_to_dataframe():
    # Load inventory data from JSON file and convert to DataFrame format
    # Assuming the JSON structure is a list of items with keys: name, cost_price, selling_price, quantity, category
    try:
        with open('data/inventory.json', 'r') as file:
            inv_json_data = json.load(file)
        for i in inv_json_data:
            for i in inv_json_data[i]:
                inventory_item = [i['name'], i['cost_price'], i['selling_price'], i['quantity'], i['category']]
                inventory.append(inventory_item)
            return inventory
    except FileNotFoundError:
        print("Inventory file not found. Loading sample data.\n")
        create_inventory_file()
        inventory_to_dataframe()

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Main function to run the inventory management system
    clear_screen()

    print("--------------------------------")
    print("Inventory Management System")
    print("--------------------------------")

    print("Initializing inventory data...\n")
    inventory_to_dataframe()
    inventory_columns = ['Name', 'Cost', 'Value', 'Quantity', 'Category']
    inventory_data_frame = pd.DataFrame(inventory, columns=inventory_columns)
    print(inventory_data_frame)


main()