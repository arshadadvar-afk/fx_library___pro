import random

file = open("member.txt", 'w')
file.close()
file2 = open("book.txt", 'w')
file2.close()
class Book:
    def __init__(self, name, author, book_id, category, is_borrowed):
        self.name = name
        self.author = author
        self.book_id = book_id
        self.category = category
        self.is_borrowed = is_borrowed

    def show(self) :
        print(f"{self.name} - {self.author} - {self.book_id} - {self.category} - {self.is_borrowed}")


class Member :
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books = []

    def show(self):
        print(F"{self.name} - {self.member_id} - {self.books}")


class Library :
    def __init__(self):
        self.books = []
        self.member = []

    def load_file_member (self):
        with open("member.txt", 'r') as file :
            files = file.readlines()
            for i in files:
                i = i.strip()
                i = i.split(" - ")
                books2 = i[2]
                obj = Member(i[0], int(i[1]))
                if books2 != "[]":
                    books2 = books2[1:-1]
                    books3 = books2.split(", ")
                    for book_id in books3:
                        obj.books.append(int(book_id))
                else:
                    pass
                self.member.append(obj)

    def save_file_member (self):
        with open("member.txt", 'w') as file:
            for i in self.member:
                file.write(F"{i.name} - {i.member_id} - {i.books}\n")

    def load_file_books (self) :
        with open("book.txt", 'r') as file:
            files = file.readlines()
            for i in files:
                i = i.strip()
                i = i.split(" - ")
                i[4] = i[4] == "True"
                obj = Book(i[0], i[1], int(i[2]), i[3], i[4])
                self.books.append(obj)

    def save_file_books (self):
        with open("book.txt", 'w') as file :
            for i in self.books:
                file.write(F"{i.name} - {i.author} - {i.book_id} - {i.category} - {i.is_borrowed}\n")

    def add_book (self):
        name = input('enter book name :')
        author = input('enter author name :')
        for i in self.books:
            if name == i.name and author == i.author:
                print('this book is already add !')
                break
        else:
            book_id = random.randint(1000, 9999)
            for i in self.books:
                while book_id == i.book_id:
                    book_id = random.randint(1000, 9999)             
            category = input('enter category :')
            obj = Book(name, author, book_id, category, is_borrowed=False)
            self.books.append(obj)
            self.save_file_books()
            print(f"book id : {book_id}")
            print('add seccsseful !')

    def remove_book (self):
        try:
            book_id = int(input('enter book id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.books:
                if book_id == i.book_id and i.is_borrowed == False:
                    self.books.remove(i)
                    self.save_file_books()
                    print('remove seccsseful !')
                    break
                elif book_id == i.book_id and i.is_borrowed != False:
                    print('this book is reserved !')
                    break
            else:
                print('book not found !')

    def show_books (self):
        for i in self.books:
            i.show()

    def search_book (self):
        try:
            book_id = int(input('enter bok id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.books:
                if book_id == i.book_id:
                    i.show()
                    break
            else:
                print('book not found !')

    def add_member (self):
        name = input('enter member name :')
        member_id = random.randint(10000, 99999)
        obj = Member(name, member_id)
        self.member.append(obj)
        self.save_file_member()
        print(f'member id : {member_id}')
        print('add seccsseful !')

    def remove_member (self):
        try:
            member_id = int(input('enter member id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.member:
                if member_id == i.member_id and i.books == []:
                    self.member.remove(i)
                    self.save_file_member()
                    print('remove seccsseful !')
                    break
                elif member_id == i.member_id and i.books != []:
                    print('this member has got book !')
                    break
            else:
                print('member not found !')

    def show_members (self):
        for i in self.member:
            i.show()

    def search_member (self):
        try:
            member_id = int(input('enter member id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.member:
                if member_id == i.member_id :
                    i.show()
                    break
            else:
                print('member not found !')

    def borrowed_book (self):
        try:
            member_id = int(input('enter member id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.member:
                if member_id == i.member_id:
                    try:
                        book_id = int(input('enter book id :'))
                    except ValueError:
                        print('pelase enter number !')
                    else:
                        for book in self.books:
                            if book_id == book.book_id and book.is_borrowed == False:
                                book.is_borrowed = True
                                i.books.append(book.book_id)
                                self.save_file_member()
                                self.save_file_books()
                                print('borrowed seccsseful !')
                                break
                            elif book_id == book.book_id and book.is_borrowed != False:
                                print('book is not available !')
                                break
                        else:
                            print('book not found !')
                    break
            else:
                print('member not found !')

    def return_book (self):
        try:
            member_id = int(input('enter member id :'))
        except ValueError:
            print('please enter number !')
        else:
            for i in self.member:
                if member_id == i.member_id:
                    try:
                        book_id = int(input('enter book id :'))
                    except ValueError:
                        print('pelase enter number !')
                    else:
                        for book in self.books:
                            if book_id == book.book_id and book.is_borrowed == True and book.book_id in i.books:
                                book.is_borrowed = False
                                i.books.remove(book.book_id)
                                self.save_file_member()
                                self.save_file_books()
                                print('return seccsseful !')
                                break
                            elif book_id == book.book_id and book.is_borrowed != True and book.book_id in i.books:
                                print('book is available !')
                                break
                            elif book_id == book.book_id and book.is_borrowed == True and book.book_id not in i.books:
                                print('this book is not for this member !')
                                break
                        else:
                            print('book not found !')
                    break
            else:
                print('member not found !')



        
library = Library()
try:
    library.load_file_member()
except FileNotFoundError:
    print('please go to IDE and run this !')
else:
    library.load_file_books()

    while True:
        print('1.add book\n2.remove_book\n3.show books\n4.search book\n5.add member\n6.remove member\n7.show members\n8.search member\n9.borrow book\n10.return book\n11.exit')
        try:
            menu = int(input('enter :'))
        except ValueError:
            print('please enter number !')
        else:
            if menu == 1:
                library.add_book()

            elif menu == 2:
                library.remove_book()

            elif menu == 3:
                library.show_books()

            elif menu == 4:
                library.search_book()

            elif menu == 5:
                library.add_member()

            elif menu == 6:
                library.remove_member()

            elif menu == 7:
                library.show_members()

            elif menu == 8:
                library.search_member()

            elif menu == 9:
                library.borrowed_book()

            elif menu == 10:
                library.return_book()

            elif menu == 11:
                print('ok')
                break

            else:
                print('please enter number in the menu !')
