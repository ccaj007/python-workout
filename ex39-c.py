
class Book():
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

class Shelf():
    def __init__(self, width):
        self.books = []
        self.width = width

    def add_book(self, *books):
        for book in books:
            if self.total_width() + book.width > self.width:
                raise TooManyBookOnShelfError('Too many books!')
            self.books.append(book)

    def total_price(self):
        return sum(s.price for s in self.books)

    def has_book(self, title):
        return title in (one_book.title for one_book in self.books)

    def total_width(self):
        return sum(one_book.width for one_book in self.books)