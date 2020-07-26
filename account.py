from datetime import datetime
class BankAccount:

    def __init__(self,first_name,last_name,bank,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.bank=bank
        self.phone_number=phone_number
        self.withdrawals=[]
        self.deposits=[]
        self.balance=0

    def account_name(self):
        name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
        return name

    def deposit(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")

        if amount <=0:
            print("Sorry you cannnot deposit {} Ksh".format(amount))

        else:

            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            deposit={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance+=amount
            self.deposits.append(amount)
            print("You have deposited {} to {} at {}".format(amount,self.account_name(),formatted_time))

    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return

        if  amount <=0:
            print("Sorry,You cannot that amount")

        elif amount >=self.deposits:
            print("You do not have enough balance")

        else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            withdraw={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {} at {}".format(amount,self.account_name(),formatted_time))

    def get_balance(self):
        return "The balance for {} is {} Ksh".format(self.account_name(),self.balance)   

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            time=withdraw(['time'])
            amount=withdraw(['amount'])
            formatted_time=time.strftime("%A,%drd %B %Y, %H:%M:%P")
            w_statement="You have withdrawn {} on {}".format(amount,formatted_time)
            print(w_statement)

    def show_deposit_statement(self):
        for deposit in self.deposits:
            time=deposit(['time'])
            amount=deposit(['amount'])
            formatted_time=time.strftime("%A ,%d /%B /%Y, %H:%M:%P")
            statement="You deposited {} on {}".format(amount,formatted_time)
            print(statement)

    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount <=0:
            print("Sorry!You cannot request a loan of that amount")

        else:
            self.loan = amount
            print("You have received a loan of {}".format(amount))

    def repay_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount > self.loan:
            
            self.balance -= self.loan
            print("Your loan has been fully repaid.Your account has been credited with {}".format(self.balance))

        elif self.loan==0:
            print("You do not have a loan balance")

        elif amount <=0:
            print("Sorry,you cannot repay that amount")

        else:
            self.loan-=amount
            print("You have repaid {},Your loan balance is {}".format(amount,self.loan))               
from datetime import datetime
class BankAccount:

    def __init__(self,first_name,last_name,bank,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.bank=bank
        self.phone_number=phone_number
        self.withdrawals=[]
        self.deposits=[]
        self.balance=0

    def account_name(self):
        name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
        return name

    def deposit(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")

        if amount <=0:
            print("Sorry you cannnot deposit {} Ksh".format(amount))

        else:

            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            deposit={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance+=amount
            self.deposits.append(amount)
            print("You have deposited {} to {} at {}".format(amount,self.account_name(),formatted_time))

    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return

        if  amount <=0:
            print("Sorry,You cannot that amount")

        elif amount >=self.deposits:
            print("You do not have enough balance")

        else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            withdraw={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {} at {}".format(amount,self.account_name(),formatted_time))

    def get_balance(self):
        return "The balance for {} is {} Ksh".format(self.account_name(),self.balance)   

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            time=withdraw(['time'])
            amount=withdraw(['amount'])
            formatted_time=time.strftime("%A,%drd %B %Y, %H:%M:%P")
            w_statement="You have withdrawn {} on {}".format(amount,formatted_time)
            print(w_statement)

    def show_deposit_statement(self):
        for deposit in self.deposits:
            time=deposit(['time'])
            amount=deposit(['amount'])
            formatted_time=time.strftime("%A ,%d /%B /%Y, %H:%M:%P")
            statement="You deposited {} on {}".format(amount,formatted_time)
            print(statement)

    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount <=0:
            print("Sorry!You cannot request a loan of that amount")

        else:
            self.loan = amount
            print("You have received a loan of {}".format(amount))

    def repay_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount > self.loan:
            
            self.balance -= self.loan
            print("Your loan has been fully repaid.Your account has been credited with {}".format(self.balance))

        elif self.loan==0:
            print("You do not have a loan balance")

        elif amount <=0:
            print("Sorry,you cannot repay that amount")

        else:
            self.loan-=amount
            print("You have repaid {},Your loan balance is {}".format(amount,self.loan))               
