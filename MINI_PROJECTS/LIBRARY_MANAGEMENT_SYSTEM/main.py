from book import Book
from library import Library
from member import Member


def main():
    try:
        library = Library()
    except (OSError, ValueError) as error:
        print(error)
        return

    while True:
        print("\n======== LIBRARY MANAGEMENT SYSTEM ========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. View Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. View Borrowing Records")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")

            library.add_book(Book(book_id, book_name))

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book(input("Enter Book ID: "))

        elif choice == "4":
            member_id = input("Enter Member ID: ")
            member_name = input("Enter Member Name: ")

            library.register_member(Member(member_id, member_name))

        elif choice == "5":
            library.view_members()

        elif choice == "6":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")

            library.borrow_book(member_id, book_id)

        elif choice == "7":
            library.return_book(input("Enter Book ID: "))

        elif choice == "8":
            library.view_borrowing_records()

        elif choice == "9":
            print("Exiting Application!!!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()