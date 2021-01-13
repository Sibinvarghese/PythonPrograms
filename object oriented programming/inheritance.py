#single inheritance
class Parent:
    def phone(self):
        print("i have Oneplus 8Pro")
#inheritance is used classname(inherit class name)
class child(Parent): #child(parent) this child class is inherit from parent class
    pass

obj=child()
obj.phone()


