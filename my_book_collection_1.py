# Un-implied Sequence implementation.

class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.next = None


class BookCollection:
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


# Test Code
if __name__ == "__main__":
    my_book_collection = BookCollection()
    my_book_collection.add_book("The Tell-Tale Brain", "V.S. Ramachandran")
    my_book_collection.add_book("Phantoms in the Brain", "V.S. Ramachandran")
    my_book_collection.add_book("The Joy of X", "Steven Strogatz")
    my_book_collection.add_book("Outliers", "Malcom Gladwel")
    my_book_collection.add_book("The Invisible Man", "H.G. Wells")

    for book in my_book_collection:
        print(book)

    for book in my_book_collection:
        print(book)

    print(my_book_collection[3])
    print(len(my_book_collection))