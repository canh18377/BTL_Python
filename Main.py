from LibraryManagement import LibraryManagement
from Book import Book
from Member import Member

# Khởi tạo hệ thống
library = LibraryManagement()

# Thêm sách
book1 = Book('B001', 'Python Basics', 'John Doe', 'Programming', 10)
book2 = Book('B002', 'Django for Beginners', 'Jane Smith', 'Programming', 5)
library.add_book(vars(book1))

def main():
    library = LibraryManagement()
    while True:
        print("\n📚 HỆ THỐNG QUẢN LÝ THƯ VIỆN")
        print("1. Thêm sách")
        print("2. Thêm thành viên")
        print("3. Mượn sách")
        print("4. Trả sách")
        print("5. Hiển thị danh sách sách")
        print("6. Hiển thị danh sách thành viên")
        print("7. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == "1":
            book_id = input("Mã sách: ")
            title = input("Tên sách: ")
            author = input("Tác giả: ")
            genre = input("Thể loại: ")
            quantity = int(input("Số lượng: "))
            book = Book(book_id, title, author, genre, quantity)
            library.add_book(vars(book))
            print("table sach:")
            print(library.get_books_dataframe())
        
        elif choice == "2":
            member_id = input("Mã thành viên: ")
            name = input("Tên: ")
            phone = input("SĐT: ")
            id_card = input("CCCD: ")
            address = input("Địa chỉ: ")
            library.add_member(Member(member_id, name, phone, id_card, address))
            print(library.get_members_dataframe())
        
        elif choice == "7":
            break
main()