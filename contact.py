#lab 1 - module 3
contact_book = {}

while True:
    print("\n=Welcome to the contact book=")
    print("============Options==========")
    print("1.Add Contact")
    print("2.Delete contact")
    print("3.View all contacts")
    print("4.Find contact")
    print("5.Exit")

    choice = int(input("Select one of the 5 options:"))

    if choice == 1:
        key = input("Enter name:")
        value = input("Enter Phone number")
        contact_book[key] = value

        print(contact_book)

    elif choice == 2:
        
        delete = input(("Enter name to delete"))
        if delete in contact_book:
            del contact_book[delete]
        else:
            print("Key not found")

        print(contact_book)

    elif choice == 3:
        for name,contact in contact_book.items():
            print(name,contact)

    elif choice == 4:

        search = input("Enter name or contact to search:")

        if search.lower() in contact_book:
            print("Name:",search)
            print("Contact number:",contact_book[search])

        elif search in contact_book.values():
            for name,values in contact_book.items():
                if values == search:
                    print("Name:",name)
                    print("Contact:",values)
        else:
            print("Contact not found")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid choice")
    