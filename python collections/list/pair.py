lst=[1,3,4,2]
lst.sort()
#print(lst)
element=int(input("enter element"))
low=0
upp=len(lst)-1
#print(upp)
while(low<upp):
    total=lst[low]+lst[upp]

    if(total==element):
        print("Pairs",lst[low],lst[upp])
        break

    elif(total>element):
        upp=upp-1
    elif(total>element):
        low=low+1