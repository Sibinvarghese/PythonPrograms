lst=[2,3,5]
temp=[]
count=1
sum=0
for item in lst:
    sum=item**count
    temp.append(sum)
    #print(sum)
    count+=1
print(temp)

