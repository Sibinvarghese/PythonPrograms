lst=[4,1,2,5,6,7]
newlst=[]
for item in lst:
    if(item>5):
        temp=item+1
        newlst.append(temp)
    elif(item<5):
        temp=item-1
        newlst.append(temp)

print(newlst)