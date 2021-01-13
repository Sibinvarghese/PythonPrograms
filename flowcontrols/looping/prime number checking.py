num1=int(input("enter the number"))
flag=0
for i in range(2,num1):
 if(num1%i==0):
     flag=1
     break
 else:
     flag=0
     break
if(flag>0):
    print("not prime")
else:
    print("prime")