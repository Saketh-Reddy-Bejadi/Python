#Class(simplier format)
class Student:
    RollNo=0
    Name=""
    Marks=0.00  
    def changename(newname):
        Name=newname  
student=Student()  
student.changename(6) 
print(student.RollNo)
print(student.Name)
print(student.Marks)
print(student)
print(Student)



#Classes using __init__ function which is used to assign values t variables
class Student:
    def __init__(new,name,rollNo,marks):
        new.name=name
        new.rollNo=rollNo
        new.marks=marks
    def __str__(new):
        return f"name:{new.name}\nRollno:{new.rollNo}\nMarks:{new.marks}"
    def prinme(new):
        print(f"\n{new.name}\n{new.rollNo}\n{new.marks}")
    def changename(new,newname):
        new.name=newname
s1=Student("Saketh Reddy","22R01A66D5",89.5)
s1.changename("rohit")
print(s1)
s1.prinme()







