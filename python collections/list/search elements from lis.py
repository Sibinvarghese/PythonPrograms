lst=[10,11,12,13,14,15,16,17,12,19,12]
search1=int(input("enter the search values"))
val1=0
for item in lst:
    if(search1==item):
        val1=1
        break
    else:
        val1=0

if(val1>0):
    print("Is found")
else:
    print("Is not found")
