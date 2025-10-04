import pandas as pd
import json

inventory = []

def inventory_to_dataframe():
    
    with open('data/inventory.json', 'r') as file:
        inv_json_data = json.load(file)
    for i in inv_json_data:
        for i in inv_json_data[i]:
            inventory_item = [i['name'], i['cost_price'], i['selling_price'], i['quantity'], i['category']]
            inventory.append(inventory_item)
        return inventory

inventory_to_dataframe()

inventory_columns = ['Name', 'Cost', 'Value', 'Quantity', 'Category']
df = pd.DataFrame(inventory, columns=inventory_columns)
print(df)

