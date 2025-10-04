import pandas as pd
import json
import os
from rich.table import Table
from rich.console import Console
import gc

inventory = []

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
    inventory = []
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
        return inventory_to_dataframe()

def build_inventory_table():
    # Build and return a DataFrame representation of the inventory
    clear_screen()
    inventory = inventory_to_dataframe()
    inventory_columns = ['Name', 'Cost', 'Value', 'Quantity', 'Category']
    inventory_data_frame = pd.DataFrame(inventory, columns=inventory_columns)
    return inventory_data_frame

def display_table(old_inventory_data_frame):
    del old_inventory_data_frame
    gc.collect()
    new_inventory_data_frame = build_inventory_table()
    #print(new_inventory_data_frame)
    table = Table(show_header=True, header_style="bold magenta", title="Inventory")
    for column in new_inventory_data_frame.columns:
        table.add_column(column, style ="cyan", width=12, no_wrap=True)
    for row in new_inventory_data_frame.iterrows(): 
        row = row[1]  # Extract the Series from the tuple
        item_list = [] 
        for i in row.values:
            item_list.append(i)
        table.add_row(*[str(i) for i in item_list])
    console = Console()
    console.print(table)

def main_menu(inventory_data_frame):
    # Display the main menu options
    print("--------------------------------")
    print("Inventory Management System")
    print("--------------------------------")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please select a valid option.")
        clear_screen()
        return main_menu(inventory_data_frame)
    else:
        if choice == '1':
            clear_screen()
            print("Initializing inventory data...\n")
            display_table(inventory_data_frame)
            input("\nPress Enter to return to the main menu...")
            clear_screen()
            main_menu(inventory_data_frame)
        elif choice == '2':
            print("Add Item functionality not implemented yet.")
        elif choice == '3':
            print("Remove Item functionality not implemented yet.")
        elif choice == '4':
            print("Update Item functionality not implemented yet.")
        elif choice == '5':
            print("Exiting the program.")
            exit()
    return 

def Startup(inventory_data_frame):
    # Main function to run the inventory management system
    clear_screen()
    main_menu(inventory_data_frame)

inventory_data_frame = build_inventory_table()
Startup(inventory_data_frame)