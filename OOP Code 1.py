class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print("{} course added for {}.".format(course, self.name))

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print("{} course removed for {}.".format(course, self.name))
        else:
            print("{} is not enrolled in the {} course.".format(self.name, course))

    def display_info(self):
        print("Student ID: ",self.student_id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Courses Enrolled:")
        if self.courses:
            for course in self.courses:
                print(course)
        else:
            print("No courses enrolled.")

#Driver code:
student = None

while True:
    print("\n\n\n")
    print("=======Student Management Menu=======")
    print("1. Add Student")
    print("2. Enroll Student in Course")
    print("3. Remove Student from Course")
    print("4. Display Student Information")
    print("5. Exit")

    inp = input("Enter your choice (1-5): ")

    if inp == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student = Student(student_id, name, age)
        print("Student added successfully.")

    elif inp == "2":
        if student is None:
            print("No student added. Add a student first.")
            continue
        course = input("Enter the course name: ")
        student.add_course(course)

    elif inp == "3":
        if student is None:
            print("No student added yet. Please add a student first.")
            continue
        course = input("Enter the course name: ")
        student.remove_course(course)

    elif inp == "4":
        if student is None:
            print("No student added yet. Please add a student first.")
            continue
        student.display_info()

    elif inp == "5":
        print("Exiting the Student Management Menu...")
        break

    else:
        print("Invalid choice. Please try again.")