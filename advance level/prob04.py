'''- Build a simple Library Management System
- Classes: `Book`, `Member`, `Library`
- Track borrowed books and members '''


# Book class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id}) - {'Borrowed' if self.is_borrowed else 'Available'}"


# Member class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member {self.name} (ID: {self.member_id})"


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member}")

    def borrow_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not book:
            print("Book not found.")
        elif not member:
            print("Member not found.")
        elif book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed {book.title}")

    def return_book(self, book_id, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not member:
            print("Member not found.")
            return

        book = next((b for b in member.borrowed_books if b.book_id == book_id), None)

        if not book:
            print("Book not found in member's borrowed list.")
        else:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            print(f"{member.name} returned {book.title}")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)
