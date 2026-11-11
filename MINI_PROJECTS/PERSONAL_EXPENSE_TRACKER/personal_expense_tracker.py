# one transaction will contain this info. 
#{
#     "type": "expense",
#     "amount": 500,
#     "category": "Food",
#     "description": "Dinner"
# }

import json
from pathlib import Path 

class PersonalExpenseTracker:

    def __init__(self):
        self.transactions = []
        self.file_path = Path(__file__).resolve().parent / "transactions.json"

        if self.file_path.exists():
            self.load_personal_expense()
        else:
            self.save_personal_expense()

    def save_personal_expense(self):
        data = {
            "transactions" : self.transactions
        }

        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4)

    def load_personal_expense(self):
        with open(self.file_path,"r",encoding="utf-8") as file:
            data = json.load(file)

        self.transactions = data["transactions"]

    def add_transactions(self,transaction_type,amount,category,description):
        if transaction_type not in ("income","expense"):
            print("Invalid Type.")
            return
        try:
            amount=float(amount)
        except(ValueError,TypeError):
            print("Invalid amount.")
            return
        if amount<=0:
            print("Amount should be greater than zero.")
            return

        new_data = {
                    "type" : transaction_type,
                    "amount" : amount,
                    "category" : category,
                    "description" : description
                }

        self.transactions.append(new_data)
        self.save_personal_expense()

        print(f"{transaction_type.capitalize()} added successfully!")

        
    def view_all_transactions(self):
        if not self.transactions:
            print("No Transactions Present.")
            return
        for transaction in self.transactions:
            print(f"Type : {transaction['type']} | "
                   f"Category : {transaction['category']} | "
                   f"Amount : {transaction['amount']} | "
                   f"Description : {transaction['description']}"
                  
                  )
        print("=======================================")

    def check_balance(self):
        total_income = 0
        total_expense = 0

        for transaction in self.transactions:
            if(transaction['type'] == "income"):
                total_income += transaction['amount']
            elif(transaction['type'] == "expense"):
                total_expense += transaction['amount']
        remaining_balance = total_income - total_expense
        return {
        "total_income": total_income,
        "total_expense": total_expense,
        "remaining_balance": remaining_balance
            }


    def filter_by_category(self,category):
        found = False

        for transaction in self.transactions:
            if category.strip().lower() == transaction['category'].strip().lower():
                print(f"Type : {transaction['type']} | " f"Category : {transaction['category']} | " f"Amount : {transaction['amount']} | " f"Description : {transaction['description']}")
                found = True
        if not found:
            print("Provided category does not exist.")

    #Approach 2 = def filter_by_category(self, category):
    # filtered_transactions = []
    # for transaction in self.transactions:
    #     if transaction["category"].strip().lower() == category.strip().lower():
    #         filtered_transactions.append(transaction)

    # return filtered_transactions

    def spending_summary(self):
        category_totals = {}
        for transaction in self.transactions:
            if(transaction['type'] == "expense"):
                category = transaction['category']
                amount = transaction['amount']

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
        return category_totals

    def sort_transactions(self,descending=False):
        sorted_list = sorted(self.transactions,key=lambda x : x['amount'],reverse=descending)
        return sorted_list
    # sorted() performs traversing internally so for loop is not needed to get amount from dictionary.
