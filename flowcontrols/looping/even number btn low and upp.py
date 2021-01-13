num1=int(input("enter th lower limit"))
num2=int(input("enter the upper limit"))
if(num1>num2):
    print("upper limit sholud nr hrater than low limit")
while(num1<=num2):
    if(num1%2==0):
     print(num1)
    num1+=1