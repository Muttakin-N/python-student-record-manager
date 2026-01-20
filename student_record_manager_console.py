

def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"


def addStudent():
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    result = grade(marks)

    f = open("student.txt","a")
    f.write(name + " - " + str(marks) + " - " + result + "\n")
    f.close()

    print("Student Record Added Successfully!\n")


def viewStudent():
    try:
        f = open("student.txt","r")
        print("\n---- Student Records ----")
        for line in f:
            print(line.strip())
        f.close()
    except:
        print("No Records Found...\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter Your Choice(1/2/3): ")

        if choice == "1":
            addStudent()
        elif choice == "2":
            viewStudent()
        elif choice == "3":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice. Try again...\n")



menu()

