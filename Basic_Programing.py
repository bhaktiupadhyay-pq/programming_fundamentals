# Simple Banking System Project

bank_name = "ABC Bank"
balance = 0

transactions = []

user_name = ""
account_type = ""

account_types = ["Savings", "Current"]


# Create Account
def create_account():

    global user_name
    global account_type

    print("\n----- Create Account -----")

    user_name = input("Enter your name: ")

    print("1. Savings Account")
    print("2. Current Account")

    choice = input("Select account type: ")

    if choice == "1":
        account_type = account_types[0]

    elif choice == "2":
        account_type = account_types[1]

    else:
        account_type = "Savings"

    print("\nAccount Created Successfully")
    print("Name :", user_name)
    print("Account Type :", account_type)


# Deposit Money
def deposit():

    global balance

    print("\n----- Deposit Money -----")

    try:

        amount = float(input("Enter amount: "))

        if amount > 0:

            balance = balance + amount

            transactions.append("Deposited ₹" + str(amount))

            print("Money Deposited Successfully")

        else:
            print("Amount should be greater than 0")

    except:
        print("Invalid Input")


# Withdraw Money
def withdraw():

    global balance

    print("\n----- Withdraw Money -----")

    try:

        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:

            balance = balance - amount

            transactions.append("Withdrawn ₹" + str(amount))

            print("Withdrawal Successful")

    except:
        print("Invalid Input")


# Check Balance
def check_balance():

    print("\n----- Account Balance -----")

    print("Current Balance :", balance)


# Transaction History
def show_transactions():

    print("\n----- Transaction History -----")

    if len(transactions) == 0:

        print("No Transactions Available")

    else:

        for item in transactions:
            print(item)


# Search Transaction
def search_transaction():

    print("\n----- Search Transaction -----")

    word = input("Enter word to search: ")

    found = False

    for item in transactions:

        if word.lower() in item.lower():

            print(item)

            found = True

    if found == False:
        print("Transaction Not Found")


# Sort Transactions
def sort_transactions():

    print("\n----- Sorted Transactions -----")

    sorted_list = sorted(transactions)

    for item in sorted_list:
        print(item)


# Interest Calculation
def calculate_interest():

    print("\n----- Interest Calculation -----")

    rate = 5
    time = 2

    interest = (balance * rate * time) / 100

    print("Interest after 2 years :", interest)


# String Functions
def string_operations():

    print("\n----- String Operations -----")

    print("Uppercase :", user_name.upper())

    print("Lowercase :", user_name.lower())

    print("Length :", len(user_name))


# Pattern Printing using Nested Loop
def display_pattern():

    print("\n----- Pattern -----")

    for i in range(5):

        for j in range(i + 1):

            print("*", end=" ")

        print()


# Class and Object
class Bank:

    def display_bank(self):

        print("\nWelcome to", bank_name)


# Object Creation
obj = Bank()

obj.display_bank()


# Main Program
create_account()

while True:

    print("\n========== MENU ==========")

    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Search Transaction")
    print("6. Sort Transactions")
    print("7. Calculate Interest")
    print("8. String Operations")
    print("9. Display Pattern")
    print("10. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        show_transactions()

    elif choice == "5":
        search_transaction()

    elif choice == "6":
        sort_transactions()

    elif choice == "7":
        calculate_interest()

    elif choice == "8":
        string_operations()

    elif choice == "9":
        display_pattern()

    elif choice == "10":

        print("\nThank You For Using", bank_name)

        break

    else:

        print("Invalid Choice")

        continue


# Do While Type Loop in Python

print("\nCountdown")

count = 3

while count > 0:

    print(count)

    count = count - 1

print("Program Ended")