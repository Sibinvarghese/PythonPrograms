class Student():
    def __init__(self,roll,name,course,mark):
        self.rollno=roll
        self.name=name
        self.course=course
        self.total=mark

    def printStudent(self):
        print("roll no=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
        print("TotalMark=",self.total)

    def __str__(self):
        return self.name

f=open("studentlist","r")
lst=[]
for item in f:
    data=item.rstrip("\n").split(",")
    #print(data)
    rollno=data[0]
    name=data[1]
    course=data[2]
    mark=int(data[3])
    obj1=Student(rollno,name,course,mark)
    lst.append(obj1)

#print all items
# for items in lst:
#     print(items)

#print all student name who have total>150

# for obj in lst:
#     if(obj.total>450):
#         print(obj)

#highest mark of student in this list
total=[]
for obj in lst:
    total.append(obj.total)
#print(max(total))
maximum=max(total)
for total in lst:
    if(total.total==maximum):
        print(total)


#convert all employee name upper case
names=list(map(lambda obj:obj.name.upper(),lst))
print(names)

#print all student name who have total>150
total=list(filter(lambda obj:obj.total>450,lst))
for i in total:
    print(i)



