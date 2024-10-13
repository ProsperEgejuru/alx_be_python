# shopping_list_manager.py

def display_menu():
    """Displays the menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ").strip()  # Get the user's choice
        
        if choice == '1':  # Add item to the list
            item = input("Enter the name of the item to add: ").strip()
            shopping_list.append(item)  # Add the item to the list
            print(f"{item} has been added to the shopping list.")
            
        elif choice == '2':  # Remove item from the list
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")
                
        elif choice == '3':  # View the current shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")  # Display each item in the list
            else:
                print("The shopping list is currently empty.")
                
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break  # Exit the loop and terminate the program
            
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()
