class Book:
    def __init__(self, color, book_size):
        self.color = color
        self.book_size = book_size

    def get_book_color(self):
        return self.color

    def calculate_books_price(self, book_page_number):
        if type(self) == Romance:
            page_price = 1.5
        else:
            page_price = 1
        return int(book_page_number) * page_price


class Fiction(Book):
    def __init__(self, name, color, book_size, page_number):
        Book.__init__(self, color, book_size)
        self.name = name
        self.page_number = page_number

    def get_fiction_price(self):
        return Book.calculate_books_price(self, self.page_number)


class Romance(Fiction):
    def __init__(self, name, color, book_size, page_number=100):
        Fiction.__init__(self, name, color, book_size, page_number)


fiction1 = Fiction("alchemist", "red", "large", 150)
romance = Romance("hary potter", "blue", "large")
print(romance.get_fiction_price())

