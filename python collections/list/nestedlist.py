employee=[
          [100,"sibin",35000],
          [101,"shahabas",25000],
          [102,"fanoob",30000],
          [103,"vyshak",25000],
          [104,"ranjan",265000]
        ]
#print all data
# for data in employee:
#     print(data)
#
# #print all employee name only
# for data in employee:
#     print(data[1])
#
# #calculate sum of salary
# sum=0
# for data in employee:
#     #print(data[2])
#     sum=sum+data[2]
# print(sum)

#print all employee name who have salary > 25000
# for data in employee:
#     if(data[2]>25000):
#         print(data[1])

#print least +ve missing integer
lst=[-1,0,1,3,4]
temp=0
for i in range(0,len(lst)):
    if(temp in lst):
        pass
    else:
        print(temp,"is the least +ve missing number")
        break
    temp+=1




