"""Day 010: OOP

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-13. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance:
            raise ValueError("invalid amount or insufficient funds")
        self.balance -= amount

account = BankAccount("Anaya", 1000)
account.deposit(250)
account.withdraw(400)
print(account.owner, account.balance)
