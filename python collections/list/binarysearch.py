ar=[5,3,2,6,1,4]
ar.sort()
print(ar)
low=0
flag=0
upp=len(ar)
element=int(input("enter the search element"))
while(low<upp):
    mid=(low+upp)//2
    if(element>ar[mid]):
        low=mid+1
    elif(element<ar[mid]):
        upp=mid-1
    elif(element==ar[mid]):
        flag=1
        break
if(flag>0):
    print("found")
else:
    print("not found")