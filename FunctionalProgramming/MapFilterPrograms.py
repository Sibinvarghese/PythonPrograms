# def squares(num):
#     return num*num
# numbers=[1,2,3,4,5,6,7,8,9]
# #using map() function
# #MAP() have 2 Arguments function and iterable..
# #in this situation function is squares and iterable is numbers
# data=list(map(squares,numbers))
# print(data)
#
# def even(num):
#     return num%2==0
#
# #Filter() Function is Used
# #Filter() have 2 Arguments function and iterable..
# #in this situation function is even and iterable is numbers
# evens=list(filter(even,numbers))
# print(evens)


#Replace by lambda
numbers=[1,2,3,4,5,6,7,8,9]
data=list(map(lambda num:num*num,numbers))
print(data)
evens=list(filter(lambda num:num%2==0,numbers) )
print(evens)


#print all character to uppercase
names=["kkr","dc","kxp","mi","csk"]

chars=list(map(lambda num1:num1.upper(),names))
print(chars)


#REDUCE FUNCTION

from functools import *
numbers1=[10,28,79,37,46]

total=reduce(lambda num1,num2:num1+num2,numbers1)
print(total )

max=reduce(lambda num1,num2:num1 if num1>num2 else num2,numbers1)
print(max)