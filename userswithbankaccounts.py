class BankAccount:
        
        def __init__(self, int_rate=0.02, balance=0):
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                self.balance -= amount
                return self

        def display_account_info(self):
                print(self.balance)
                return self

        def yield_interest(self):
                self.balance += self.balance * self.int_rate
                return self

class User:
        def __init__(self, name, email_address):
                self.name = name
                self.email = email_address
                self.account = BankAccount(int_rate = .02, balance = 0)

        def make_deposit(self, amount):
                self.account.deposit(amount) 
                return self

        def make_withdrawal(self, amount):
                self.account.withdraw(amount)
                return self
    
        def display_user_balance(self):
                print("User:" , self.name , ", Balance:" , self.account.balance)
                return self


blair = User("Blair", "blairyoung009@gmail.com")
blair.make_deposit(1000).make_withdrawal(200).display_user_balance()