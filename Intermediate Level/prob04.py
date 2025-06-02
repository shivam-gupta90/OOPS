# - Create a class `Book` with ISBN, name, author, and price
# - Implement `__eq__()` to compare two books based on ISBN

class Book:
    def __init__(self,isbn,author,price):
        self.isbn = isbn
        self.author = author
        self.price = price
    def __str__(self):
        return f"Name of author :{self.author}  ISBN :{self.isbn}  price:{self.price}"
    
    def __eq__(self,other):
        if isinstance(self,Book):
           return self.isbn == other.isbn
        return False  


book1 =Book("2432","kapil",200)
book2 = Book("2432","sham",400)

# Comparing them
if book1 == book2:
    print("The books are the same (based on ISBN).")
else:
    print("The books are not the same (based on ISBN).")
print(book1)
print(book2)