# Implied Sequence implementation.

from collections.abc import Sequence


class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.next = None


# Sequence interface ensures implementation of __len__ and __getitem__
class MyBookCollection2(Sequence):  # Class making its intent clear
    def __init__(self):
        self.books = None
        self.books_count = 0

    def add_book(self, book_name, author):
        new_book = Book(book_name, author)
        if self.books is None:
            self.books = new_book
        else:
            current = self.books
            while current.next is not None:
                current = current.next
            current.next = new_book
        self.books_count += 1

    def __len__(self):
        return self.books_count

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Invalid Index Type")
        if item > self.books_count - 1:
            raise IndexError("Books: Index Out of Range")
        index = 0
        current = self.books
        while index < item:
            index += 1
            current = current.next
        return f"{current.book_name}, by - {current.author}"


# Test code
if __name__ == "__main__":
    my_book_collection = MyBookCollection2()
    my_book_collection.add_book("The Tell-Tale Brain", "V.S. Ramachandran")
    my_book_collection.add_book("Phantoms in the Brain", "V.S. Ramachandran")
    my_book_collection.add_book("The Joy of X", "Steven Strogatz")
    my_book_collection.add_book("Outliers", "Malcom Gladwel")
    my_book_collection.add_book("The Invisible Man", "H.G. Wells")

    print(len(my_book_collection))
    print(my_book_collection[0])

    for book in my_book_collection:
        print(book)

    for book in my_book_collection:
        print(book)
    print(my_book_collection[2])