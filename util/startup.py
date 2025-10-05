
from util.build_inventory_table import display_inventory_table
from util.table_manager import add_inventory_item, update_inventory_item
from util.core import clear_screen


def MainMenu():
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
        return MainMenu()
    else:
        if choice == '1':
            clear_screen()
            display_inventory_table()
            input("\nPress Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '2':
            clear_screen()
            add_inventory_item()
            input("\nItem added. Press Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '3':
            print("Remove Item functionality not implemented yet.")
        elif choice == '4':
            clear_screen()
            update_inventory_item()
            input("\nItem updated. Press Enter to return to the main menu...")
            MainMenu()
        elif choice == '5':
            print("Exiting the program.")
            exit()
    return 