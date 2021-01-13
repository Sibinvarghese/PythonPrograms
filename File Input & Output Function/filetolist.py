f=open("number file.txt","r")
temp=[]
for numbers in f:
    #remove \n
    numbers=int(numbers.rstrip("\n"))
    temp.append(numbers)

print(temp)
# #find the sum of list
total=sum(temp)
print("Sum OF List ",total)
# #find the maximum number of list
maxi=max(temp)
print("Maximum number from list ",maxi)
#find the miniimum number of list
mini=min(temp)
print(" Maximum number from list  ",mini)



