#  Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
	def __init__ (self, interest_rate, balance): # don't forget to add some default values for these parameters!
                self.interest_rate = interest_rate
                self.balance = balance
      
# don't worry about user info here; we'll involve the User class soon

#  Add a deposit method to the BankAccount class
	def deposit(self, amount):
                self.balance += amount
                return self

#  Add a withdraw method to the BankAccount class
	def withdraw(self, amount):
                if self.balance < amount:
                        print("Insufficient funds: Charging a $5 fee")
                        self.balance -= amount + 5
                else:
                        self.balance -= amount
                return self

#  Add a display_account_info method to the BankAccount class   
	def display_account_info(self):
                print("Balance: $" + str(self.balance))
                return self

#  Add a yield_interest method to the BankAccount class
	def yield_interest(self):
                if self.balance > 0:
                        self.balance = (self.balance * self.interest_rate) + self.balance
                return self
#  Create 2 accounts
irisChecking = BankAccount(0.02, 1000)
irisSavings = BankAccount (0.10,1000)

#  To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
irisChecking.deposit(500).deposit(500).deposit(0).withdraw(900).yield_interest().display_account_info()

#  To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)

irisSavings.deposit(100).deposit(300).withdraw(50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()