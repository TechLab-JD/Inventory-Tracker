from util.core import clear_screen

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