class Parent1:
    def m1(self):
        print("inside parent1")

class Parent2:
    def m1(self):
        print("inside parent2")
#chilapo situvation il inherit cheyumbo 
class child(Parent1,Parent2):
    def m2(self):
        print("inside child")

c=child()
c.m2()
c.m1()