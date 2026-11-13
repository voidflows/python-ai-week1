import json
from datetime import datetime
from pathlib import Path

from book import Book
from loan import Loan
from member import Member


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []
        self.file_path = Path(__file__).resolve().parent / "books.json"

        if self.file_path.exists():
            self.load_data()
        else:
            self.save_data()

    def save_data(self):
        data = {
            "books": {
                book_id: book.to_dict()
                for book_id, book in self.books.items()
            },
            "members": {
                member_id: member.to_dict()
                for member_id, member in self.members.items()
            },
            "loans": [
                loan.to_dict() for loan in self.loans
            ]
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Saved data must be a JSON object")

            saved_books = data.get("books", {})
            saved_members = data.get("members", {})
            saved_loans = data.get("loans", [])

            if (
                not isinstance(saved_books, dict)
                or not isinstance(saved_members, dict)
                or not isinstance(saved_loans, list)
            ):
                raise ValueError("Invalid books, members, or loans structure")

            books = {}

            for book_id, details in saved_books.items():
                # Support JSON from the earlier version
                if isinstance(details, str):
                    books[book_id] = Book(book_id, details)
                else:
                    books[book_id] = Book(
                        book_id,
                        details["name"],
                        details.get("available", True)
                    )

            members = {}

            for member_id, details in saved_members.items():
                if isinstance(details, str):
                    members[member_id] = Member(member_id, details)
                else:
                    members[member_id] = Member(
                        member_id,
                        details["name"]
                    )

            loans = [
                Loan(**details) for details in saved_loans
            ]

            self.books = books
            self.members = members
            self.loans = loans

        except (OSError, ValueError, TypeError, KeyError) as error:
            raise ValueError(
                f"Unable to load {self.file_path}: {error}"
            ) from error

    # 1. ADD BOOK
    def add_book(self, book):
        if not book.book_id or not book.book_name:
            print("Book ID and name cannot be empty.")

        elif book.book_id in self.books:
            print("Book already exists!")

        else:
            self.books[book.book_id] = book
            self.save_data()
            print("Book added successfully!")

    # 2. VIEW ALL BOOKS
    def view_books(self):
        if not self.books:
            print("No Books Available.")
            return

        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"

            print(
                f"Book ID: {book.book_id} | "
                f"Name: {book.book_name} | {status}"
            )

    # 3. SEARCH BOOK
    def search_book(self, book_id):
        book = self.books.get(book_id.strip().upper())

        if book is None:
            print("No Such Book Available.")
        else:
            status = "Available" if book.available else "Borrowed"

            print(
                f"Book ID: {book.book_id} | "
                f"Name: {book.book_name} | {status}"
            )

    # 4. REGISTER MEMBER
    def register_member(self, member):
        if not member.member_id or not member.member_name:
            print("Member ID and name cannot be empty.")

        elif member.member_id in self.members:
            print("Member already registered!")

        else:
            self.members[member.member_id] = member
            self.save_data()
            print("Member registered successfully!")

    # 5. VIEW MEMBERS
    def view_members(self):
        if not self.members:
            print("No Members Registered.")
            return

        for member in self.members.values():
            print(
                f"Member ID: {member.member_id} | "
                f"Name: {member.member_name}"
            )

    # 6. BORROW BOOK
    def borrow_book(self, member_id, book_id):
        member_id = member_id.strip().upper()
        book_id = book_id.strip().upper()

        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books.get(book_id)

        if book is None:
            print("Book not found.")
            return

        if not book.available:
            print("Book is already borrowed.")
            return

        loan = Loan(
            f"L{len(self.loans) + 1:03d}",
            book_id,
            member_id,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.loans.append(loan)
        book.available = False
        self.save_data()

        print(
            f"Book borrowed successfully! "
            f"Loan ID: {loan.loan_id}"
        )

    # 7. RETURN BOOK
    def return_book(self, book_id):
        book_id = book_id.strip().upper()
        book = self.books.get(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.available:
            print("This book is not currently borrowed.")
            return

        for loan in reversed(self.loans):
            if loan.book_id == book_id and loan.returned_at is None:
                loan.returned_at = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                book.available = True
                self.save_data()

                print("Book returned successfully!")
                return

        print("No active borrowing record found.")

    # 8. VIEW BORROWING RECORDS
    def view_borrowing_records(self):
        if not self.loans:
            print("No Borrowing Records Available.")
            return

        for loan in self.loans:
            status = "Returned" if loan.returned_at else "Borrowed"

            print(
                f"{loan.loan_id} | "
                f"Book: {loan.book_id} | "
                f"Member: {loan.member_id} | {status}"
            )

            print(
                f"Borrowed: {loan.borrowed_at} | "
                f"Returned: {loan.returned_at or '-'}"
            )