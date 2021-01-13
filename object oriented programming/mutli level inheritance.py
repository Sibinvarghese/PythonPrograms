#mutli level inheritance
#one parent class and two child class

class Parent:
    def m1(self):
        print("inside parent")

class child(Parent):
    def m2(self):
        print("inside child")

class subchild(child):
    def m3(self):
        print("inside subchild")

sb=subchild()
sb.m3()
sb.m2()
sb.m1()