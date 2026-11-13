class Loan:
    def __init__(self, loan_id, book_id, member_id, borrowed_at, returned_at=None):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.borrowed_at = borrowed_at
        self.returned_at = returned_at

    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "borrowed_at": self.borrowed_at,
            "returned_at": self.returned_at
        }