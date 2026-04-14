class BankAccount:
  def __init__(self, owner):
    self.owner = owner
    self.balance = 0

  def deposit(self, amount):
    self.balance = self.balance + amount
    print(f" this is your balance {self.balance}")

    bankaccount = BankAccount("david")

    bankaccount.deposit()