# Write Python programs to demonstrate different types of inheritance 
# (single, multiple,multilevel, etc.)

#base class
class Person:
    def __init__(self,name,c_no,address):
        self.name=name
        self.c_no=c_no
        self.address=address
    def display(self):
        print(f"{self.name} - {self.c_no} - {self.address}")

#single inheritance
class Student(Person):
    def __init__(self, name, c_no, address,roll_no,marks):
        super().__init__(name, c_no, address)
        self.roll_no=roll_no
        self.marks=marks
    def displayStudent(self):
        print(f"{self.roll_no} - {self.name} - {self.address} - {self.c_no} - {self.marks}")

#multilevel inheritance
class CollegeStudent(Student):
    def __init__(self, name, c_no, address, roll_no, marks,collage_name):
        super().__init__(name, c_no, address, roll_no, marks)
        self.collage_name=collage_name
    def display(self):
        print(f"{self.name} - {self.c_no} - {self.address} - {self.roll_no} - {self.roll_no} - {self.marks} - {self.collage_name}")

#separate class
class Company:
    def __init__(self,c_name,c_address,c_id):
        self.c_name=c_name
        self.c_address=c_address
        self.c_id=c_id
    def display_c(self):
        print(f"{self.c_name} - {self.c_address} - {self.c_id}")

#multiple class 
class Employee(Student,Company):
    def __init__(self, name, c_no, address, roll_no, marks,e_name,c_id):
        super().__init__(name, c_no, address, roll_no, marks)
        self.e_name=e_name
        self.c_id=c_id
    def display(self):
        print(f"{self.name} - {self.c_no} - {self.address} - {self.roll_no} - {self.e_name} - {self.c_id}")


obj=Student("Kunal",1234,"Paldi",23,200)
obj.displayStudent()

obj1=Student("Mahesh",2232,"CGRoad",45,220)
obj1.displayStudent()

obj2=CollegeStudent("Mahesh",2232,"CGRoad",45,220,"tops")
obj2.display() 

obj3=Employee("ravi",234,"baloch",67,45,"ravi",9)
obj3.display()
