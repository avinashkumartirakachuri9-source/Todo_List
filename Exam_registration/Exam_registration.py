def exam_registration():
    subjects=[]
    while True:
        print("\nAvailable Subjects")
        print("1. Maths")
        print("2. Physics")
        print("3. Electronics")
        print("4. PLC")
        print("5. Done")
        choice=input("Select subject number: ")
        if choice=="1":
            subjects.append("Maths")
        elif choice=="2":
            subjects.append("Physics")
        elif choice=="3":
            subjects.append("Electronics")
        elif choice=="4":
            subjects.append("PLC")
        elif choice=="5":
            break
        else:
            print("Invalid subject")
    return subjects
def total_fee(subjects):
    fee=len(subjects)*400
    print(f"Total Exam Fee: {fee}")
students=[]
print("------- Exam Registration System -------")
while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. Register Subjects")
    print("3. View Students")
    print("4. Calculate Fee")
    print("5. Exit")
    option=input("Enter option: ")
    if option=="1":
        name=input("Enter Student Name: ")
        roll=input("Enter Roll Number: ")
        course=input("Enter Course: ")
        student={
            "name":name,
            "roll":roll,
            "course":course,
            "subjects":[]
        }
        students.append(student)
        print("Student added successfully")
    elif option=="2":
        roll=input("Enter Roll Number: ")
        for student in students:
            if student["roll"]==roll:
                student["subjects"]=exam_registration()
                print("Subjects registered")
                break
        else:
            print("Student not found")
    elif option=="3":
        print("\nStudents List")
        for i,stu in enumerate(students,1):
            print(i,stu)
    elif option=="4":
        roll=input("Enter Roll Number: ")
        for student in students:
            if student["roll"]==roll:
                total_fee(student["subjects"])
                break
        else:
            print("Student not found")
    elif option=="5":
        print("Thank you for using the system")
        break
    else:
        print("Invalid option")