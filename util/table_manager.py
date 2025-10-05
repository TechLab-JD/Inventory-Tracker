import json
import time

from util.core import clear_screen

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

def list_of_items():
    # Return a list of item names in the inventory
    with open('data/inventory.json', 'r') as file:
        data = json.load(file)
        return [item['name'] for item in data['items']]

def item_details(item_name):
    # Return the details of a specific item
    with open('data/inventory.json', 'r') as file:
        data = json.load(file)
        item_exists = any(item['name'] == item_name for item in data['items'])
        if not item_exists:
            print(f"Item '{item_name}' not found in inventory.")
            return
    clear_screen()
    item_info = (f"""
    --------------------------------
    \t\tItem Details:
    --------------------------------
    Item Name: {item_name}
    Cost: {next(item['cost_price'] for item in data['items'] if item['name'] == item_name)}
    Value: {next(item['selling_price'] for item in data['items'] if item['name'] == item_name)}
    Quantity: {next(item['quantity'] for item in data['items'] if item['name'] == item_name)}
    Category: {next(item['category'] for item in data['items'] if item['name'] == item_name)}        
    --------------------------------""")
    return item_info

def update_inventory_item():
    # Update an existing item in the inventory table
    with open('data/inventory.json', 'r') as file:
        data = json.load(file)    
    print("Current items in inventory:")
    for i in list_of_items():
        print(f"- {i}")
    item_name = input("Enter item name: ")
    print(item_details(item_name))
    print("Are you sure you want to update this item? (y/n)")
    confirm = input("Select an option: ")
    if confirm.lower() == 'y':       
        print("What would you like to update?")
        print("""
1. Cost Price
2. Selling Price
3. Quantity
4. Category
5. Name
6. All
7. Cancel
        """)
        choice = input("Select an option (1-7): ")
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice. Please select a valid option.")
            return update_inventory_item()
        elif choice == '1':
            print(f"""
Updating Cost Price
    Current Cost Price: {next(item['cost_price'] for item in data['items'] if item['name'] == item_name)}    
            """)
            new_cost_price = float(input("Enter new cost price: "))
            updated_item = {
                "name": item_name,
                "cost_price": new_cost_price,
            }
        elif choice == '2':
            print(f"""
Updating Selling Price
    Current Selling Price: {next(item['selling_price'] for item in data['items'] if item['name'] == item_name)}
            """)
            new_selling_price = float(input("Enter new selling price: "))
            updated_item = {
                "name": item_name,
                "selling_price": new_selling_price,
            }
        elif choice == '3':
            print(f"""
Updating Quantity
    Current Quantity: {next(item['quantity'] for item in data['items'] if item['name'] == item_name)}
            """)
            new_quantity = int(input("Enter new quantity: "))
            updated_item = {
                "name": item_name,
                "quantity": new_quantity,
            }
        elif choice == '4':
            print(f"""
Updating Category   
    Current Category: {next(item['category'] for item in data['items'] if item['name'] == item_name)}
            """)
            new_category = input("Enter new category: ")
            updated_item = {
                "name": item_name,
                "category": new_category,
            }  
        elif choice == '5':
            print(f"""
Updating Name
    Current Name: {item_name}
            """)
            new_name = input("Enter new name: ")
            updated_item = {
                "name": new_name,
            }
        elif choice == '6':
            print(f"""
Updating All Details
    Current Details:
    Name: {item_name}
    Cost Price: {next(item['cost_price'] for item in data['items'] if item['name'] == item_name)}
    Selling Price: {next(item['selling_price'] for item in data['items'] if item['name'] == item_name)}
    Quantity: {next(item['quantity'] for item in data['items'] if item['name'] == item_name)}
    Category: {next(item['category'] for item in data['items'] if item['name'] == item_name)}
            """)

            new_name = input("Enter new name: ")
            new_cost_price = float(input("Enter new cost price: "))
            new_selling_price = float(input("Enter new selling price: "))
            new_quantity = int(input("Enter new quantity: "))
            new_category = input("Enter new category: ")
            updated_item = {
                "name": new_name,
                "cost_price": new_cost_price,
                "selling_price": new_selling_price,
                "quantity": new_quantity,
                "category": new_category
            }
        elif choice == '7':
            print("Update cancelled.")
            return

        with open('data/inventory.json', 'r+') as file:
            data = json.load(file)
            for i, item in enumerate(data['items']):
                if item['name'] == item_name:
                    data['items'][i].update(updated_item)
                    break
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        print(item_details(item_name))


        print("Would you like to continue updating items?")
        option = input("Enter 'y' to continue or any other key to exit: ")
        if option.lower() == 'y':
            clear_screen()
            return update_inventory_item()
        else:
            print("Exiting update menu.")
            return
    else:
        print("Update cancelled.")
        
        return
