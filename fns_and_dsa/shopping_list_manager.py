
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
            shopping_list.append(input("Enter an item to add: "))
            pass
        elif choice == 2:
            # Prompt for and remove an item
            shopping_list.remove(input("Enter an item to remove: "))
            pass
        elif choice == 3:
            # Display the shopping list
            shopping_list.sort()
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()