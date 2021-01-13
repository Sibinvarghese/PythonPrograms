class Employee():
    def __init__(self,id,name,desig,sal):
        self.id=id
        self.name=name
        self.designation=desig
        self.salary=sal

    def printemployee(self):
        print("id=",self.id )
        print("name=",self.name)
        print("designation=",self.designation)
        print("salary=",self.salary )

    def __str__(self):
        return self.name

f=open("employeelist","r")
lst=[]
for items in f:
    data=items.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    course=data[2]
    salary=int(data[3])
    obj1=Employee(id,name,course,salary)
    lst.append(obj1)

# for items in lst:
#     print(items)

#print the highest salary of employee
# salary=[]
# for obj in lst:
#     salary.append(obj.salary)
# #print(salary)
# highestsalary=max(salary)
# #print(highestsalary)
# for slry in lst:
#     if(slry.salary==highestsalary):
#         print(slry)

#find all employee whos designation => developer
# for items in lst:
#     if(items.designation=='developer'):
#         print(items)
des=list(filter(lambda obj1:obj1.designation=="developer",lst))
for d in des:
    print(d)
#print(des)
#convert all employee name upper case
upp=list(map(lambda obj:obj.name.upper(),lst))
print(upp)
#
# #find total salary of all employee
from functools import *
allsal=reduce(lambda num1,num2:num1+num2,list(map(lambda obj:obj.salary,lst)))
print(allsal)

#find highest salaried employee name
sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda obj:obj.salary,lst)))
print(sal)


