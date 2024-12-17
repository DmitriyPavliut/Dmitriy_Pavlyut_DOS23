class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} пополнено. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"{amount} снято. Новый баланс: {self.balance}")