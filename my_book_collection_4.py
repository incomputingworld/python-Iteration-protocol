# Iterator implementation using iterator class

class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.next = None


class BooksIterator:  # Iterator class
    def __init__(self, books):
        self.books = books
        self.current = self.books

    def __next__(self):
        if self.current is None:
            raise StopIteration
        book_details = f"{self.current.book_name}, by - {self.current.author}"
        self.current = self.current.next
        return book_details


class MyBookCollection4:  # Iterable
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

    def __iter__(self):
        book_iter = BooksIterator(self.books)
        return book_iter


if __name__ == "__main__":
    my_book_collection = MyBookCollection4()
    my_book_collection.add_book("The Tell-Tale Brain", "V.S. Ramachandran")
    my_book_collection.add_book("Phantoms in the Brain", "V.S. Ramachandran")
    my_book_collection.add_book("The Joy of X", "Steven Strogatz")
    my_book_collection.add_book("Outliers", "Malcom Gladwel")
    my_book_collection.add_book("The Invisible Man", "H.G. Wells")

    books_iter1 = iter(my_book_collection)
    books_iter2 = iter(my_book_collection)
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")
    print(f"books_iter1 - {next(books_iter1)}")
    print(f"books_iter2 - {next(books_iter2)}")
    print(f"books_iter1 - {next(books_iter1)}")  # raises StopIteration exception

