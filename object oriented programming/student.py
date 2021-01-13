class Student():
    def getValues(self,id,name,course,total):
        self.id=id
        self.name=name
        self.course=course
        self.total=total
    def printValues(self):
        print("Roll No=",self.id)
        print("name=",self.name)
        print("Course=", self.course)
        print("total=",self.total)
obj=Student()
obj.getValues(101,"Sibin","MCA",78)
obj.printValues()
