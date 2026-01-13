# print("A")
# print("B")
# print("c")

# balance = 1000
# balance = 2900
# print(balance)

# a = 10
# b = a
# a = 20
# print(b)

# x = True
# print(type(x))

# first = "hello"
# second = "world"
# print(first +" "+ second)

# first = "Hello"
# second = "my name is david"
# third = "and"
# fourth = "i am learning python"
# fifth = " "
# print(first+fifth+second+fifth+third+fifth+fourth)

# name = input("Enter your Name: ")
# print(name)

# ATM = input("Enter your balance: ")
# print(ATM)

# This takes in the name of the user
name = input("Enter your name: ")
# This collects the balance
balance = int(input("enter your account balance: "))
# This collects the withdrawal amount
withdraw = int(input("Enter the amount you choose to withdraw:"))
# This collets the amount the user wants to deposit
deposit = int(input("Enter the amount you want to deposit: "))
# This is a print function that prints out the lot 

new_balance = deposit + balance - withdraw
print(f"hello {name} welcome to GT bank tha amount you deposited is {deposit} and chose to withdraw is {withdraw} leaving your balance at {new_balance}")


