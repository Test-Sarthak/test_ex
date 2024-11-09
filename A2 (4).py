def add_student():
    name=input("Enter the student name : ")
    roll_no=int(input("Enter the student Roll no. : "))
    grade=float(input("Enter the grade of the student :"))
    student=[name,roll_no,grade]
    with open("students.txt","a") as file:
        file.write(f"{name},{roll_no},{grade}\n")


def search_student():
    rollno=int(input("Enter the roll no. to search :"))
    try:
        with open("students.txt","r") as file:
            for line in file:
                name,roll_no,grade=line.strip().split(",")
                if int(roll_no)==rollno:
                    print(f"Name : {name}\n")
                    print(f"Grade : {grade}\n")
                    return
            else:
                print("Student not found")
    except FileNotFoundError:
        print("No students added yet....\n\n")
    

while True:
    print("Enter '1' to add new student")
    print("Enter '2' to find student")
    print("Enter '3' to Exit")

    choice=int(input("Enter your choice : "))
    if choice==1:
        add_student()
    elif choice==2:
        search_student()
    elif choice==3:
        break
    else:
        print("Invalid Choice")
        print("Try again ...")



print("hello")