# 🏦 Capstone Project 2: OOP Banking Simulation

import random

# 1. Base Class: Account (Encapsulation)
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance # Protected (accessible by children)
        self.acc_number = random.randint(10000, 99999)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount} | New Balance: ${self._balance}")
        else:
            print("Amount must be positive!")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: ${amount} | Remaining Balance: ${self._balance}")
        else:
            print("Insufficient funds!")

    def get_info(self):
        return f"User: {self.owner} | Acc: {self.acc_number} | Bal: ${self._balance}"

# 2. Inherited Class: SavingsAccount (Inheritance)
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest Applied: ${interest} | New Total: ${self._balance}")

# 🚀 Use Case & Simulation
if __name__ == "__main__":
    # user1 = SavingsAccount("Chayan", 1000)
    # print(user1.get_info())
    # user1.deposit(500)
    # user1.apply_interest()
    # user1.withdraw(200)
    # print(user1.get_info())
    pass

# Summary of Features Used
"""
| Concept      | Use Case                                         |
|--------------|--------------------------------------------------|
| Encapsulation| _balance is protected inside the class          |
| Abstraction  | Users don't need to know 'how' balance updates  |
| Inheritance  | SavingsAccount gets all features of Account    |
| Randomness   | Account number generated using random.randint() |
"""
