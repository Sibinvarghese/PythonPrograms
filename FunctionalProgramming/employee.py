class employee():
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

f=open("employee","r")
lst=[]
for items in f:
    data=items.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    designation=data[2]
    salary=int(data[3])
    obj1=employee(id,name,designation,salary)
    lst.append(obj1)

#find all employee whos designation => developer
result=[emp.name for emp in lst if emp.designation=="developer"]
print(result)

#convert all employee name upper case

upp=[obj.name.upper() for obj in lst]
print(upp)
# #find total salary of all employee
sumsal=sum([obj1.salary for obj1 in lst])
print(sumsal)

#find highest salaried employee name

maxx=max([obj1.salary for obj1 in lst])
print(maxx)