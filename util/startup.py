
from util.build_inventory_table import display_inventory_table
from util.table_manager import add_inventory_item, update_inventory_item, remove_inventory_item, export_inventory
from util.core import clear_screen
from util.data_analyze import analyze_inventory, search_inventory

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
    print("5. Analyze Inventory")
    print("6. Export Inventory")
    print("7. Search Inventory")
    print("8. Exit")
    choice = input("Select an option (1-5): ")
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Invalid choice. Please select a valid option.")
        input("Press Enter to continue...")
        clear_screen()
        return MainMenu()
    else:
        if choice == '1':
            clear_screen()
            display_inventory_table()
            input("Press Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '2':
            clear_screen()
            add_inventory_item()
            input("\nItem added. Press Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '3':
            clear_screen()
            remove_inventory_item()
            input("\nItem removed. Press Enter to return to the main menu...")
            MainMenu()
        elif choice == '4':
            clear_screen()
            update_inventory_item()
            input("\nItem updated. Press Enter to return to the main menu...")
            MainMenu()
        elif choice == '5':
            clear_screen()
            analyze_inventory()
            input("\nPress Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '6':
            clear_screen()
            print("Exporting inventory...")
            export_inventory()
            input("\nInventory exported. Press Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '7':
            clear_screen()
            search_inventory()
            input("\nPress Enter to return to the main menu...")
            clear_screen()
            MainMenu()
        elif choice == '8':
            print("Exiting the program.")
            exit()
    return 