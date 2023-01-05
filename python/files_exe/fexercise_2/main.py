def create_book_list_file():
    with open(r'C:\Users\devops\Desktop\2\books.txt', 'w') as books_file:
        book_name = input('enter your book name here: ')
        while book_name != 'stop':
            book_auther = input('enter the name of book auther: ')
            books_file.write(book_name + ' by ' + book_auther + '\n')
            book_name = input('enter your book name here: ')


if __name__ == "__main__":
    create_book_list_file()