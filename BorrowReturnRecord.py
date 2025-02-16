from datetime import datetime, timedelta

class BorrowReturnRecord:
    def __init__(self, record_id, member_id, borrowed_books, borrow_date=None):
        self.record_id = record_id
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        self.borrow_date = borrow_date or datetime.now()
        self.expected_return_date = self.borrow_date + timedelta(days=14)
        self.actual_return_date = None

    # def return_books(self, return_date):
    #     self.actual_return_date = return_date
    #     overdue_days = max((return_date - self.expected_return_date).days, 0)
    #     fine = overdue_days * 5000  # Phí trễ hạn: 5000đ/ngày
    #     return fine

