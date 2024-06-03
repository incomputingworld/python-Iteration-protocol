# Iterable Iterator implementation

class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.next = None


class MyBookCollection3:
    def __init__(self):
        self.books = None
        self.books_count = 0
        self.current = None

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

    def __iter__(self):
        self.current = self.books
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        book_details = f"{self.current.book_name}, by - {self.current.author}"
        self.current = self.current.next
        return book_details


# Test code
if __name__ == "__main__":
    my_book_collection = MyBookCollection3()
    my_book_collection.add_book("The Tell-Tale Brain", "V.S. Ramachandran")
    my_book_collection.add_book("Phantoms in the Brain", "V.S. Ramachandran")
    my_book_collection.add_book("The Joy of X", "Steven Strogatz")
    my_book_collection.add_book("Outliers", "Malcom Gladwel")
    my_book_collection.add_book("The Invisible Man", "H.G. Wells")

    # two iterator objects, referring to the same iterable.
    books_iter1 = iter(my_book_collection)
    books_iter2 = iter(my_book_collection)

    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")  # raises StopIteration exception
