class Library:
    def __init__(self):
        self.file = open('books.txt', 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            print('List of Books:')
            for book in books:
                title, author, year, pages = book.strip().split(',')
                print(f'Title: {title}, Author: {author}')
        else:
            print('No books available.')

    def add_book(self):
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        while True:
            year = input('Enter release year: ')
            if not year.isdigit():
                print('Invalid input. Year must be an integer.')
            else:
                break
        while True:
            pages = input('Enter number of pages: ')
            if not pages.isdigit():
                print('Invalid input. Pages must be an integer.')
            else:
                break
        self.file.write(f'{title},{author},{year},{pages}\n')
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title = input('Enter the title of the book to remove: ')
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        updated_books = []
        for book in books:
            if title not in book:
                updated_books.append(book)
            else:
                found = True
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found.")


lib = Library()

while True:
    print('\n*** MENU ***')
    print('1) List Books')
    print('2) Add Book')
    print('3) Remove Book')
    print('4) Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4' or choice == 'q' or choice == 'Q':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please choose again.')
