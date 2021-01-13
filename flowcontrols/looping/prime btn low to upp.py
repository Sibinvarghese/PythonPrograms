low=int(input("enter the low limit"))
upp=int(input("enter the upp limit"))
for i in range(low,upp):
    for j in range(2,i):
        if(i%j==0):
         break
    else:
     print(i)
