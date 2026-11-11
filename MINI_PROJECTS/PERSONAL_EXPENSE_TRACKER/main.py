from personal_expense_tracker import PersonalExpenseTracker

tracker = PersonalExpenseTracker()

while True:
    print("\n=========PERSONAL EXPENSE TRACKER===================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Check Balance")
    print("5. Filter by category")
    print("6. Spending Summary")
    print("7. Sort Transactions")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        tracker.add_transactions("income", amount, category, description)

    elif choice == 2:
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        tracker.add_transactions("expense", amount, category, description)

    elif choice == 3:
        print("\n========== ALL TRANSACTIONS ==========")
        tracker.view_all_transactions()

    elif choice == 4:
        balance_details = tracker.check_balance()
        print("\n===========BALANCE SUMMARY=================")
        print(f"Total Income     : ₹{balance_details['total_income']:.2f}")
        print(f"Total Expenses   : ₹{balance_details['total_expense']:.2f}")
        print(f"Remaining Balance: ₹{balance_details['remaining_balance']:.2f}")

    elif choice == 5:
        category = input("Enter category you are looking for : ")
        tracker.filter_by_category(category)

    elif choice == 6:
        summary = tracker.spending_summary()
        if not summary:
            print("No expenses found.")
        else:
            print("\n========== SPENDING SUMMARY ==========")
            for category, amount in summary.items():
                print(f"{category} : ₹{amount:.2f}")

            total_spending = sum(summary.values())

            print("--------------------------------------")
            print(f"Total Spending : ₹{total_spending:.2f}")

    elif choice == 7:
         print("1. Low to High")
         print("2. High to Low")

         choice = input("Enter sorting choice: ")

         if choice == "1":
            transactions = tracker.sort_transactions(False)
         elif choice == "2":
            transactions = tracker.sort_transactions(True)
         else:
            print("Invalid choice.")
            continue

         for transaction in transactions:
            print(transaction)
            
    elif choice == 8:
        print("Exiting application.")
        break
    else:
        print("Invalid Choice.Please try again")