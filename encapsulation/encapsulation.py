class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Test
acc = BankAccount("Obi", 500)
acc.deposit(200)
print(acc.get_balance())  # 700

# acc.__balance  ← This will give an error (private variable)