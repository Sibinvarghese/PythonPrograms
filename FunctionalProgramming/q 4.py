#list Comprihension
lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = []
for item in lst:
    for item2 in lst2:
        print(item,item2)
        #lst3.append(item,item2)
#print(lst3)

oupt=[(i,j) for i in lst for j in lst2]
print(oupt)
#print the squares of nubers
lst4=[1,2,3,4,5,6]
squares=[(i*i) for i in lst4]
print(squares)
#To print even numbers
even=[i for i in lst4 if i%2==0]
print(even)
#To print the cube of a numbers
# lst5=[1,2,3,4,5,6]
# cube=[(i*3) for i in lst5]
# print(cube)

oupt=[i+1 if i>5 else i-1 for i in lst4]
print(oupt)