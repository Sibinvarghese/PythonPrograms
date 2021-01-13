class Bank:
    bank_name="SBK" #static variable
    def createAccount(self,acno,pname):
        self.accountname=acno
        self.personname=pname
        self.balance=3000
    def desposit(self,amount):
        self.balance+=amount
        print("Your",Bank.bank_name,"has been credited with",amount,"availabe balance is",self.balance )
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insuffient balance in your account")
        else:
            self.balance-=amount
            print("Your",Bank.bank_name, "has been credited with", amount, "availabe balance is", self.balance)

    def balanceEnq(self):
        print("Your availabe balance is", self.balance)
obj=Bank()
obj.createAccount(101,"Sibin",)
obj.desposit(10000)
obj.withdraw(3000)
obj.balanceEnq()