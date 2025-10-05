from util.core import clear_screen
from util.table_manager import list_of_items

import json


def analyze_inventory():
    # Analyze the inventory data and print statistics
    with open('data/inventory.json', 'r') as file:
        data = json.load(file)
        items = data['items']
        name_list = [item['name'] for item in items]
        category_list = list(set(item['category'] for item in items))
        total_items = len(items)
        total_categories = len(category_list)
        total_quantity = sum(item['quantity'] for item in items)
        total_inventory_value = sum(item['cost_price'] * item['quantity'] for item in items)
        total_potential_revenue = sum(item['selling_price'] * item['quantity'] for item in items)
        total_potential_profit = total_potential_revenue - total_inventory_value
        average_profit_margin = (total_potential_profit / total_inventory_value * 100) if total_inventory_value > 0 else 0
    print(f"""
--------------------------------
\tInventory Analysis
--------------------------------
Total items: {total_quantity}

Inventory value:  ${total_inventory_value:.2f}  
Potential revenue:  ${total_potential_revenue:.2f} 
--------------------------------
Total potential profit:  ${total_potential_profit:.2f}

Avg profit margin:  {average_profit_margin:.2f}%
--------------------------------
{total_categories} Categories: 
{', '.join(category_list)}

{total_items} Unique items: 
{', '.join(name_list)}
--------------------------------""") 

def search_inventory():
    # Search for an item in the inventory and display its details
    item_name = input("Enter the item name to search (or 'All' to list all items):  \n>> ")
    with open('data/inventory.json', 'r') as file:
        data = json.load(file)
        items = data['items']
        item = next((item for item in items if item['name'].lower() == item_name.lower()), None)
        if item:
            print(f"""
--------------------------------
\tItem Details>> '{item_name}'
--------------------------------
Cost Price: ${item['cost_price']:.2f}
Selling Price: ${item['selling_price']:.2f}
Quantity: {item['quantity']}
Category: {item['category']}
--------------------------------""")
        elif item_name == '':
            print("Item name cannot be empty.")
            input("Press Enter to try again...")
            clear_screen()
            return search_inventory()
        elif item_name.lower() == "all":
            alphabetical_items = sorted(list_of_items(), key=lambda x: x.lower())
            for i in alphabetical_items:
                print(f"- {i}")
            return search_inventory()
        else:
            print(f"Item '{item_name}' not found in inventory.")
