def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

shopping_list = []

while True:
    display_menu()
    choice =int(input("choose a number that represents your choice: "))
    if choice == 1:
        add = input("Enter the item to add: ").lower()
        shopping_list.append(add)
    elif choice == 2:
        remove = input("Choose an item to remove from the list: ").lower()
        if remove in shopping_list:
            shopping_list.remove(remove)
        else:
            print("you entered an invalid input")
    
    elif choice == 3:
        print(shopping_list)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4")



