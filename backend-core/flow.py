password = 1234
if password == 1234:
  print("Access granted")
else:
  print("Access denied")

balance = 400000000
if balance >= 10000000:
  print("premium account")
else:
  print("basic account")  

score = 49

if score>=70:
  print("Excellent")
elif score >= 50:
  print("good")
else:
  print("fail")    

loan = 69

if loan>= 750:
  print("approved")
elif loan>= 600:
  print("review")
else:
  print("rejected")  

balance = -5000
account_active = True

if balance > 0 and account_active:
  print("Transaction allowed")
else:
  print("Fuck you broke ass nigga")  

balance = 150
card_active = True

if balance >= 1000 and card_active:
  print("Withdraw allowed")
else:
  print("Transaction denied")

balance = 1500
card_active = True

if card_active:
  if balance >= 1000:
    print("withdrawal successful")
  else:
    print("insuffient funds")
else:
  print("card blocked")

balance = 3000
card_active = True
pin_correct = True

if card_active:
  if balance >= 0 and pin_correct :
    print("withdrawal successful")
  else:
    print("please retry")
else:
  print("block account")

# THIS IS THE MINI PROJECT


password = int(input("enter password here: "))
balance = 20000000

if password == 1234:
  amount = int(input("Enter amount to withdraw: "))

  if amount <= balance:
    balance -= amount
    print("withdrawal successful")
    print("remaining balance: ", balance)

  else:
    print("insufficent funds")

else:
  print("incorrect pin")


