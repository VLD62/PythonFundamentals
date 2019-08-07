class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = float(price)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,value):
        if len(value) < 3:
            print('Title not valid!')
            exit(0)
        else:
            self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self,value):
        if len(value.split()) > 1 and value.split()[1][0].isdigit():
            print('Author not valid!')
            exit(0)
        else:
            self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value <= 0:
            print('Price not valid!')
            exit(0)
        else:
            self.__price = value



    def __str__(self):
        return  f"""\
Type: Book
Title: {self.title}
Author: {self.author}
Price: {self.price:.2f}
"""


class GoldenEditionBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author,price)

    def __str__(self):
        return  f"""\
Type: GoldenEditionBook
Title: {self.title}
Author: {self.author}
Price: {(self.price + 0.3 * self.price):.2f}
"""

if __name__ == "__main__":
    author = input()
    title = input()
    price = input()
    newBook = Book(title=title,author=author,price=price)
    newGoldenBook = GoldenEditionBook(title=title,author=author,price=price)
    print(newBook)
    print(newGoldenBook)
