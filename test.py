"""
MINI ATM SYSTEM
"""

# ------------------ LOGIN FUNCTION ------------------
def login():
    attempts = 0
    while attempts < 3:
        password = input("Enter your password: ")
        if password == "1234":  # correct password
            print("Login successful!")
            return True  # login succeeded
        else:
            attempts += 1
            print(f"Wrong password. {3 - attempts} attempts left.")
    return False  # all attempts used

# ------------------ CHECK BALANCE FUNCTION ------------------
def check_balance(balance):
    print(f"Your balance is: {balance}")

# ------------------ DEPOSIT FUNCTION ------------------
def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    if amount <= 0:
        print("Invalid amount. Deposit must be positive.")
        return balance  # return original balance
    else:
        balance += amount
        print(f"Deposit successful! New balance: {balance}")
        return balance

# ------------------ WITHDRAW FUNCTION ------------------
def withdraw(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount. Withdrawal must be positive.")
        return balance
    elif amount > balance:
        print("Insufficient funds!")
        return balance
    else:
        balance -= amount
        print(f"Withdrawal successful! New balance: {balance}")
        return balance

# ------------------ MAIN ATM PROGRAM ------------------
if login():  # only run menu if login succeeds
    current_balance = 1200  # initial balance

    while True:
        print("\nATM Menu")
        print("1: Check balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(current_balance)
        elif choice == "2":
            current_balance = deposit(current_balance)
        elif choice == "3":
            current_balance = withdraw(current_balance)
        elif choice == "4":
            print("Thank you for using the ATM!")
            break  # exit loop
        else:
            print("Invalid choice, try again.")

else:
    print("Failed login. Exiting...")
