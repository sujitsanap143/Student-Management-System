class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No : {self.roll}\n"\
               f"Name : {self.name}\n"\
               f"Marks : {self.marks}"

students_list = []
    
def add_student():
    roll = int(input("Enter Roll No : "))
    name = input("Enter Name : ")
    marks = float(input("Enter Marks : "))
    stu = Student(roll, name, marks)
    students_list.append(stu)
    print("Student Added")

def show_student():
    for stu in students_list:
        print(stu)

def choices(student_change):
    ch = int(input("What do you want to Update?\n"\
                   "1 : Name\n"\
                   "2 : Marks\n"\
                   ))
    match ch:
        case 1:
            newname = input("Enter New Name = ")
            student_change.name = newname
            print("Name Updated")
        case 2:
            newmarks = float(input("Enter New Marks = "))
            student_change.marks = newmarks
            print("Marks Updated")

def update_student_info():
    roll = int(input("Enter Roll No : "))
    student_change = False
    for student in students_list:
        if student.roll == roll:
            student_change = student
            break
    if student_change:
        choices(student_change)
    else:
        print("No Such Roll No Found")

def delete_student_info():
    roll = int(input("Enter Roll No : "))
    student_change = False
    for student in students_list:
        if student.roll == roll:
            student_change = student
            print("Student Deleted")
            break
    if student_change:
        students_list.remove(student_change)
    else:
        print("No Such Roll No Found")

while True:
    ch = int(input("Enter Choice : \n"\
                   "1 : Add Student \n"\
                   "2 : Show Student Info \n"\
                   "3 : Update Student Info \n"\
                   "4 : Delete Student Info \n"\
                   "5 : Exit\n"))

    match ch:
        case 1:
            add_student()
        case 2:
            show_student()
        case 3:
            update_student_info()
        case 4:
            delete_student_info()
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid Choice")

        
    















            
            
