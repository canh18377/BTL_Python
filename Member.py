class Member:
    def __init__(self, member_id, name, phone, id_card, address):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.id_card = id_card
        self.address = address
        self.borrowed_books = {}
    
    # def borrow_book(self, book_id, quantity):
    #     if len(self.borrowed_books) >= 5:
    #         return False
    #     self.borrowed_books[book_id] = self.borrowed_books.get(book_id, 0) + quantity
    #     return True

    # def return_book(self, book_id, quantity):
    #     if book_id in self.borrowed_books:
    #         self.borrowed_books[book_id] -= quantity
    #         if self.borrowed_books[book_id] <= 0:
    #             del self.borrowed_books[book_id]
