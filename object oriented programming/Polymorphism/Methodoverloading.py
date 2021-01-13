from smtplib import LMTP


class Maths:
    def add(self):
        num1,num2=10,20
        print(num1+num2)
    def add(self,num1):
        num2=50
        print(num1+num2)
    def add(self,num1,num2): # This is Called recently implemented method
        print(num1+num2)

obj=Maths()
obj.add(10,20)
# obj.add(30)
# obj.add()