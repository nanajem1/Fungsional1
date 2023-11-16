class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return f'\"{title}\" by {author} Telah Ditambahkan ke Library.'

    def display_books(self):
        available_books = [f'{idx}. \"{book.title}\" by {book.author}' 
                           for idx, book in enumerate(self.books, start=1) 
                           if book.is_available]
        borrowed_books = [f'{idx}. \"{borrowed_book.title}\" dipinjam oleh {user}' 
                          for idx, (user, borrowed_book) 
                          in enumerate(self.borrowed_books, start=1)]
        return {
            'available_books': available_books,
            'borrowed_books': borrowed_books
        }

    def borrow_book(self, user, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    self.borrowed_books.append((user, book))
                    return f'{user} Meminjam \"{title}\"'
                else:
                    return f'\"{title}\" sudah dipinjam'
        return f'\"{title}\" tidak ditemukan di perpustakaan.'

    def return_book(self, user, title):
        for i, (borrower, book) in enumerate(self.borrowed_books):
            if borrower == user and book.title == title:
                book.is_available = True
                del self.borrowed_books[i]
                return f'{user} Mengembalikan \"{title}\"'
        return f'{user} Ndak Bisa Kembalikan \"{title}\"'

def main():
    library = Library()

    while True:
        print('\n\t Main Menu')
        print('===========================================')
        print('\t 1. Login as Admin')
        print('\t 2. Login as User')
        print('\t 3. Exit')
        choice = input('Enter Your Choice: ')
        print('-------------------------------------------')

        if choice == "1":
            admin_key = input('Enter Admin Pass: ')
            if admin_key == "halo":
                admin_menu(library)
            else:
                print('Invalid Pass.')
        elif choice == "2":
            user_name = input('Enter User Name: ')
            user_menu(library, user_name)
        elif choice == "3":
            print('\t Thanks')
            print('-------------------------------------------')
            break
        else:
            print('Pilihan Invalid, Sila Coba Lagi.')

def admin_menu(library):
    while True:
        print('\n\t Admin Menu')
        print('===========================================')
        print('\t 1. Tambah Buku')
        print('\t 2. Lihat Daftar Buku')
        print('\t 3. Exit')
        admin_choice = input('Enter Your Choice: ')
        print('-------------------------------------------')

        if admin_choice == "1":
            title = input('Masukkan Judul Buku: ')
            author = input('Masukkan Author: ')
            result = library.add_book(title, author)
            print(result)
        elif admin_choice == "2":
            result = library.display_books()
            print('-------------------------------------------')
            print('Buku Yang Tersedia di Library:')
            for book in result['available_books']:
                print(book)
            print('\nBuku Yang Sedang Dipinjam:')
            for book in result['borrowed_books']:
                print(book)
        elif admin_choice == "3":
            break
        else:
            print('Pilihan Invalid, Sila Coba Lagi')

def user_menu(library, user):
    while True:
        print(f'\n\t User Menu ({user})')
        print('===========================================')
        print('\t 1. Pinjam Buku')
        print('\t 2. Kembalikan Buku')
        print('\t 3. Exit')
        user_choice = input('Enter Your Choice: ')
        print('-------------------------------------------')
        
        if user_choice == "1":
            result = library.display_books()
            print('-------------------------------------------')
            print('Buku Yang Tersedia di Library:')
            for book in result['available_books']:
                print(book)
            print('\nBuku Yang Sedang Dipinjam:')
            for book in result['borrowed_books']:
                print(book)
            title = input('\nInput Judul Buku Yang Ingin Dipinjam (Ketik "batal" untuk Membatalkan): ')
            if title.lower() == "batal":
                continue
            result = library.borrow_book(user, title)
            print(result)
        elif user_choice == "2":
            title = input('Input Buku Yang Akan Dikembalikan: ')
            result = library.return_book(user, title)
            print(result)
        elif user_choice == "3":
            break
        else:
            print('Pilihan Invalid, Sila Coba Lagi.')

if __name__ == "__main__":
    main()
