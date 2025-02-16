from datetime import datetime, timedelta
import pandas as pd
class LibraryManagement:
    def __init__(self):
        self.books =[]
        self.members = []
        self.records = []

    def add_book(self, book):
        self.books.append(book)

    # def update_book(self, book_id, **kwargs):
    #     if book_id in self.books:
    #         self.books[book_id].update_info(**kwargs)

    # def delete_book(self, book_id):
    #     if book_id in self.books:
    #         for record in self.records.values():
    #             if book_id in record.borrowed_books and record.actual_return_date is None:
    #                 return False  # Cannot delete borrowed book
    #         del self.books[book_id]
    #         return True
    #     return False
    
    # def add_member(self, member):
    #     self.members[member.member_id] = member

    # def update_member(self, member_id, **kwargs):
    #     if member_id in self.members:
    #         for key, value in kwargs.items():
    #             setattr(self.members[member_id], key, value)

    # def delete_member(self, member_id):
    #     if member_id in self.members and not self.members[member_id].borrowed_books:
    #         del self.members[member_id]
    #         return True
    #     return False

    # def borrow_books(self, record_id, member_id, borrowed_books):
    #     if member_id not in self.members:
    #         return False
    #     member = self.members[member_id]
    #     borrow_date = datetime.now()
    #     return_date = borrow_date + timedelta(days=14)
        
    #     for book_id, quantity in borrowed_books.items():
    #         if book_id in self.books and self.books[book_id].quantity >= quantity:
    #             if member.borrow_book(book_id, quantity):
    #                 self.books[book_id].quantity -= quantity
    #             else:
    #                 return False
    #         else:
    #             return False
        
    #     record = BorrowReturnRecord(record_id, member_id, borrowed_books, borrow_date, return_date)
    #     self.records[record_id] = record
    #     return True

    # def return_books(self, record_id):
    #     if record_id not in self.records:
    #         return False
    #     record = self.records[record_id]
    #     if record.actual_return_date:
    #         return False

    #     return_date = datetime.now()
    #     fine = record.return_books(return_date)
        
    #     member = self.members[record.member_id]
    #     for book_id, quantity in record.borrowed_books.items():
    #         self.books[book_id].quantity += quantity
    #         member.return_book(book_id, quantity)
    #     return fine

    def get_books_dataframe(self):
        return pd.DataFrame(self.books)

    def get_members_dataframe(self):
        return pd.DataFrame(self.members)

    def get_records_dataframe(self):
        return pd.DataFrame(self.records)

