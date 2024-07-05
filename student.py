class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def info(self):
        print("Name:", self.name)
        print("Your Marks:", self.marks)

    def result(self):
        if self.marks > 75:
            print("Passed in first class")
        elif self.marks > 50:
            print("Passed in second class")
        elif self.marks > 35:
            print("Passed")
        else:
            print("You are Fail")


n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    std = Student(name, marks)
    std.info()
    std.result()
    print("." * 20)
