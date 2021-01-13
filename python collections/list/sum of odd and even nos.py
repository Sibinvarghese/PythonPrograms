lst=[10,11,12,13,14,15,16,17]
sum1=0
sum2=0
for item in lst:
    if(item%2==0):
        sum1=sum1+item
    else:
        sum2=sum2+item

print("The sum Of Odd Number :",sum2)
print("The sum Of Even Number :", sum1)
