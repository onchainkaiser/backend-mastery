def welcome(name):
  print(f"welcome {name} to ABC bank")

welcome("Dabere")  


def deposit(balance, amount):
  new_balance = balance + amount
  print(new_balance)

deposit(30,700)

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient funds"
    else:
        return balance - amount

new_balance = withdraw(300, 500)
print(new_balance)

def loan_status(balance):
  if balance >= 4000:
    return "approved"
  elif balance >= 3500:
    return "under review"
  else:
    return "rejected" 

print(loan_status(6900))   


def audit_accounts(balances):
  valid_count = 0

  for bal in balances:
    if bal < 0:
      print("Fraud dectected")
    else:
      valid_count += 1

  print(f"valid accounts: {valid_count}")

audit_accounts([5000, -200, 300, 8000])

