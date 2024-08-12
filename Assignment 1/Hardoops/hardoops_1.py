class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == "Available":
            book.status = "Borrowed"
            self.borrowed_books.append(book)
            return f"{self.name} borrowed {book.title}."
        else:
            return f"{book.title} is not available."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.status = "Available"
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}."
        else:
            return f"{self.name} doesn't have {book.title}."

class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book.title}' added to the library."

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"Book '{book.title}' removed from the library."
        return "Book not found."

    def register_member(self, member):
        self.members.append(member)
        return f"Member '{member.name}' registered."

    def lend_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if member and book:
            return member.borrow_book(book)
        else:
            return "Member or book not found."

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if member and book:
            return member.return_book(book)
        else:
            return "Member or book not found."
library = Library()
book1 = Book("Immortals of Meluha", "Amish Tripathi", "12345")
book2 = Book("Sword of Destiny: Witcher", "Andrzej Sapkowski", "67890")
print(library.add_book(book1))
print(library.add_book(book2))

member1 = Member("Kanchan", "M001")
print(library.register_member(member1))
print(library.lend_book("M001", "12345"))
print(library.return_book("M001", "12345"))
