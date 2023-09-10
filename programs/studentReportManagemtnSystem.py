
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student_data = f"{name},{roll_number},{marks}\n"
    with open("student_data.txt", "a") as file:
        file.write(student_data)
        print("Student data added successfully!")
def display_students():
    print("===================================")
    print("|    Name      |  Roll Number |  Marks |")
    print("===================================")
    with open("student_data.txt", "r") as file:
        for line in file:
            name, roll_number, marks = line.strip().split(",")
            print(f"| {name.ljust(12)} | {roll_number.ljust(12)} | {marks.ljust(6)} |")
    print("===================================")
def main():
    while True:
        print("===== Student Report Management Systems =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
