class Book:
    def __init__(self, title, author, chapters, price, sold):
        self.title = title
        self.author = author
        self.chapters = chapters
        self.price = float(price)
        self.sold = sold

def is_float(input):
    try:
        num = float(input)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    book_store = []
    book_input = input().split(' -> ')
    total_money = 0
    result_no = []
    result_yes = []
    while not book_input[0] == 'on work':
        if len(book_input[0].split()) == 3:
            _title, _author, _price = book_input[0].split()
            _chapters = book_input[1].split(", ")
            if len(_chapters) > 0 and is_float(_price) and _price[0] != '-':
                new_book = Book(title = _title, author = _author, chapters = _chapters, price = _price, sold = False)
                if new_book.title not in [book.title for book in book_store]:
                    book_store.append(new_book)
        book_input = input().split(' -> ')
    cmd_input = input()
    while not cmd_input == 'end work':
        if cmd_input not in [book.title for book in book_store]:
            result_no.append('No such book here')
        else:
            for book in book_store:
                if book.title == cmd_input:
                    book.sold = True
                    result_yes.append(f"SOLD: {book.title} with author {book.author}. Chapters in the book {len(book.chapters)}")
                    total_money += book.price
        cmd_input = input()

    if len(result_no) > 0:
        for line in result_no:
            print(line)

    if total_money > 0:
        for line in result_yes:
            print(line)
        print(f"Money: {total_money:.2f}")
    else:
        if total_money == 0:
            print("Bad day :(")
