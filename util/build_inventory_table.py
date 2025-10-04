from util.core import clear_screen
import util.json_manager as jm
import pandas as pd

from rich.table import Table
from rich.console import Console

def create_rich_table():
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
    return table

def display_inventory_table():
    rich_table = create_rich_table()
    console = Console()
    return console.print(rich_table)

def build_inventory_table():
    # Build and return a DataFrame representation of the inventory
    clear_screen()
    inventory = jm.json_to_dataframe()
    inventory_columns = ['Name', 'Cost', 'Value', 'Quantity', 'Category']
    inventory_data_frame = pd.DataFrame(inventory, columns=inventory_columns)
    return inventory_data_frame
