class Book:
    def __init__(self, book_id, book_name, available=True):
        self.book_id = book_id.strip().upper()
        self.book_name = book_name.strip()
        self.available = available

    def to_dict(self):
        return {
            "name": self.book_name,
            "available": self.available
        }