from datetime import datetime
class Account:

    def __init__(self,first_name,last_name,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.withdrawals=[]
        self.deposits=[]
        self.balance=0

    def account_name(self):
        name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
        return name

    def deposit(self,amount):
        try:
            amount + 50
        except TypeError:
            print("Please enter amount in figures")
            return

        if amount <=0:
            print("Sorry you cannnot deposit {} Ksh".format(amount))

        else:

            time=datetime.now()
            deposit={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance+=amount
            self.deposits.append(amount)
            print("You have deposited {} to {} at {}".format(amount,self.account_name(),self.formatted_time(time)))

    def withdraw(self,amount):
        try:
            amount + 50
        except TypeError:
            print("Please enter amount in figures")
            return

        if  amount <=0:
            print("Sorry,You cannot that amount")

        elif amount >=self.deposits:
            print("You do not have enough balance")

        else:
            time=datetime.now()
            withdraw={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {} at {}".format(amount,self.account_name(),self.formatted_time(time)))

    def get_balance(self):
        return "The balance for {} is {} Ksh".format(self.account_name(),self.balance)   

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            time=withdraw(['time'])
            amount=withdraw(['amount'])
            w_statement="You have withdrawn {} on {}".format(amount,formatted_time(time))
            print(w_statement)

    def show_deposit_statement(self):
        for deposit in self.deposits:
            time=deposit(['time'])
            amount=deposit(['amount'])
            statement="You deposited {} on {}".format(amount,self.formatted_time(time))
            print(statement)
            
    def formated_time(self,time):
        return time.strftime("%A ,%d /%B /%Y, %H:%M:%P")

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
            print("Please enter repayment in figures")
            return
        if amount > self.loan:
            
            self.balance -= self.loan
            print("Your loan has been fully repaid.Your account has been credited with {}".format(self.balance))

        elif self.loan==0:
            print("You do not have a loan balance")

        elif amount <=0:
            print("Sorry,you cannot repay that amount")

        else:
            repayment={
                "time":time,
                "amount":amount
            }
            self.loan-= amount
            time=datetime.now()
            self.repay_loan.append(repayment)
            print("You have repaid {},Your loan balance is {}".format(amount,self.loan))               
    
    def loan_repayment_statement(self):
        for repayment in self.repay_loan:
            time=repayment['time']
            amount=repayment['amount']
            l_statement="You repayed {} on {}".format(amount,self.formated_time(time))
            print(l_statement)
            
class BankAccount(Account):
    
    def __init__(self,first_name,last_name,bank):
        self.bank=bank
        super().__init__(first_name,last_name,phone_number)
        
    def cash_transfers(self,amount,other_account):
        time=datetime.now()
        return "You have transfered {} to {} account".format(amount,other_account,self.get_formatted_time(time))
    
    def paybill(self,amount,paybill_number,account_number):
        time=datetime.now()
        return "You have sent {} to {} for account {} on {}".format(amount,paybill_number,account_number,self.formatted_time(time))
    
    def send_money(self,amount):
        try:
            amount + 1
        except Exception:
            print("Please enter the correct amount")
        
        if amount <= self.balance:
            print("Sorry!You must pay transaction fee")
            
        else:
            self.balance -= amount
            time=datetime.now()
            print("You have sent {} to {} on {}".format(amount,receipient,self.formatted_time(time)))
            
            
    def receive_money(self,amount):
        try:
            amount + 1
        except Exception:
            print("Please enter the correct amount")
            
            self.balance += amount
            time=datetime.now()
            print("You have received {} from {} on {}".format(amount,receipient,self.formatted_time(time)))
            
    
    
    
class MobileMoneyAccount(Account):
    
    def __init__(self,first_name,last_name,phone_number,service_provider):
        self.service_provider=service_provider
        self.airtime=[]
        super().__init__(first_name,last_name,phone_number)
        
    def buy_airtime(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter an amount in figures")
            
        if amount < self.balance:
            print("You do not have enough amount to buy airtime")
            
        else:
            self.balance -= amount
            time=datetime.now()
            airtime={
                "time":time,
                "amount":amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))
            
    def send_money(self,amount,receipient):
        try:
            amount + 1
        except Exception:
            print("Please enter the correct amount")
        
        if amount <= self.balance:
            print("Sorry!You must pay transaction fee")
            
        else:
            time=datetime.now()
            print("Confirm {} sent to {} on {}".format(amount,receipient,self.get_formatted_time(time)))
            self.balance -= amount
            print("You have sent {} to {} on {}".format(amount,receipient,self.get_formatted_time(time)))
            
            
        
        
    