class BankAcount:
  bank="KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
    return name
    
  def deposit (self, amount):
    self.balance += amount
    print("You have deposited {} to your account".format(amount)) 
    
     
  def get_balance(self, amount):
    if amount > 0:
      return "Balance for {} is {}".format(self.account_name(),self.balance)
      
    else:
      return "Cannot Finish Operation"
    
  def withdraw(self, amount):
    if amount > self.balance:
      self.balance -= amount
      print ("Insufficient Amount!!:", amount)
      return
      
    else:
      print ("Withdrawal Successful, your balance is {}". format (self.balance))
      return
      
  def display(self):
    print ("Your Net Balance = {}".format(self.balance))   
    
acc1=BankAcount ("Betty", "Njambi")
acc2=BankAcount ("Hellen", "Ivy")
print()

acc1.deposit(1000)
acc2.deposit(50)
acc1.deposit(30)
acc2.deposit(75)
print()

acc1.withdraw(500)
acc2.withdraw(10)
acc1.withdraw(7895)
acc2.withdraw(500)
print ()


print (acc1.get_balance(1030)) 
print (acc2.get_balance(0))
print ()

acc1.display()
acc2.display()



