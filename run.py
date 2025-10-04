import json
import os

from util.core import clear_screen
from util.build_inventory_table import display_inventory_table

def Startup():
    # Display the main menu options
    clear_screen()
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
        return main_menu()
    else:
        if choice == '1':
            clear_screen()
            display_inventory_table()
            input("\nPress Enter to return to the main menu...")
            clear_screen()
            main_menu()
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

Startup()