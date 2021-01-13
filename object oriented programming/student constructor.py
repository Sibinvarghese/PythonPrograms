class Student():
    college_name="lumniar"
    def __init__(self,id,name,course,total):
        self.id=id
        self.name=name
        self.course=course
        self.total=total

    def printValues(self):
        print("Roll No=",self.id)
        print("name=",self.name)
        print("College_Name=", Student.college_name )
        print("Course=", self.course)
        print("total=",self.total)
    def __str__(self):
        return  self.name
        #return self.name + str(self.total)
# obj=Student(101,"Sibin","MCA",78)
# obj.printValues()
#using method overriding
obj=Student(101,"Sibin","MCA",78)
obj1=Student(101,"COdexW","MCA",98)
print(obj)
print(obj1)
