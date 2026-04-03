# Write a Python program to create a class and access its properties using an object.
class mahesh:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"my name is {self.name} and age is {self.age}")
    def show(self,a,b):
        print("sum a and b : ",a+b)
m=mahesh("mahesh",20)
m.display()
m.show(5,6)