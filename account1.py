class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance!")
        self.balance -= amount
        print("Withdrawn:", amount)
    def show_balance(self):
        print("Current Balance:", self.balance)
initial = float(input("Enter initial balance: "))
acc = BankAccount(initial)
try:
    amt = float(input("Enter amount to deposit: "))
    acc.deposit(amt)
    amt = float(input("Enter amount to withdraw: "))
    acc.withdraw(amt)
except Exception as e:
    print("Error:", e)
acc.show_balance()
