"""
The bank account class you'll create should have methods for each of the following:

1. Accepting deposits.
2. Allowing withdrawals.
3. Showing the balance.
4. Showing the details of the account.

"""
class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "%s's account. Balance: $%.2f" % (self.name, self.balance)
    
  def deposit(self, amount):
    if amount <= 0:
      print "Some error message here"
      return
    else:
      print "%s's account. Balance: $%.2f" % (self.name, self.balance)
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount <= 0:
      print "Some error message here"
      return
    else:
      print "%s's account. Balance: $%.2f" % (self.name, self.balance)
      self.balance -=  amount
      self.show_balance()
      
      
my_account = BankAccount("Your-name-here")
print my_account
show_balance(my_account)
deposit(my_account, 2000)
withdraw(my_account, 1000)
print my_account
