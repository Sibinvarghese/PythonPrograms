def prime(low,upp):
    i=2
    for low in range(low,upp):
        temp=0
        for i in range(2,low):
            if(low%i==0):
                temp=1
                break
        if(temp==0):
            print(low)
        i+=1
low=int(input("enter the low limit"))
upp=int(input("enter the upp limit"))
if(low<upp):
    prime(low,upp)
else:
    print("lower limit is big")

