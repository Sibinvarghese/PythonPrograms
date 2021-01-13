#create class
#syntax
#class Classname:
    #methods

class Person():
    def setValues(self,ag,name):
        #self is keyword used to point current object instance variables
        self.age=ag
        self.name=name
    def printValues(self):
        print("age=",self.age)
        print("name=",self.name)
#create reference
#syntax
#refernence=Classname
obj=Person()
obj.setValues(25,"sibin")
obj.printValues()


obj1=Person()
obj1.setValues(25,"shahabas")
obj1.printValues()