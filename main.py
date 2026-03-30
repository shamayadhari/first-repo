#: Object-Oriented Design and Robust Programming in a Library Management System
# Name: Shamaya Dhariwal 
# Roll no.: 2501410020
# Class: B.Tech Cybersecurity 

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status


class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_from_file()

    # Load books from text file
    def load_from_file(self):
        try:
            f = open("books.txt", "r")
            lines = f.readlines()
            f.close()

            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    title, author, isbn, status = parts
                    self.books.append(Book(title, author, isbn, status))

        except FileNotFoundError:
            # No file yet → start empty
            self.books = []

    # Save books to text file
    def save_to_file(self):
        f = open("books.txt", "w")
        for b in self.books:
            f.write(b.title + "," + b.author + "," + b.isbn + "," + b.status + "\n")
        f.close()

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")

        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_to_file()

        print("\nBook added successfully!\n")

    def issue_book(self):
        isbn = input("Enter ISBN to issue: ")

        for b in self.books:
            if b.isbn == isbn:
                if b.status == "available":
                    b.status = "issued"
                    self.save_to_file()
                    print("Book issued!\n")
                    return
                else:
                    print("Book already issued!\n")
                    return

        print("Book not found!\n")

    def return_book(self):
        isbn = input("Enter ISBN to return: ")

        for b in self.books:
            if b.isbn == isbn:
                if b.status == "issued":
                    b.status = "available"
                    self.save_to_file()
                    print("Book returned!\n")
                    return
                else:
                    print("Book is not issued.\n")
                    return

        print("Book not found!\n")

    def display_all(self):
        if not self.books:
            print("\nNo books found.\n")
            return

        print("\n--- All Books ---")
        for b in self.books:
            print("Title:", b.title)
            print("Author:", b.author)
            print("ISBN:", b.isbn)
            print("Status:", b.status)
            print("---------------------")
        print()

    def search_book(self):
        title = input("Enter title to search: ")

        found = False
        for b in self.books:
            if title.lower() in b.title.lower():
                print("\nBook Found:")
                print("Title:", b.title)
                print("Author:", b.author)
                print("ISBN:", b.isbn)
                print("Status:", b.status)
                print()
                found = True

        if not found:
            print("No book found.\n")


def menu():
    library = LibraryInventory()

    while True:
        print("""
======= Library Menu =======
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit
============================
""")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.issue_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.display_all()
        elif choice == "5":
            library.search_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()
