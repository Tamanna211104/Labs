def display_menu():
    print("Welcome to the Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")


def option1():
    print("You chose Option 1")


def option2():
    print("You chose Option 2")


def option3():
    print("You chose Option 3")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
