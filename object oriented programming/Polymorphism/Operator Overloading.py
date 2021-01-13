class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return Book (self.pages+other.pages)

    def __sub__(self, other):
        return Book (self.pages-other.pages)

    def __mul__(self, other):
        return Book (self.pages*other.pages)

    def __truediv__(self,  other):
        return Book (self.pages/other.pages)

    def __str__(self):
        return str(self.pages)

obj=Book(300)
print(obj)

obj1=Book(100)
print(obj1)

obj2=Book(300)
print(obj+obj1+obj2)
print(obj-obj1)
print(obj*obj1+obj2)
print(obj/obj1)

