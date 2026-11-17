class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book = input("Enter book name: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name: ")
        library.return_book(book)

    elif choice == "5":
        break

    else:
        print("Invalid choice")