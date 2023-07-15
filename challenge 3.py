# Challange 3
class Student:

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber


student = Student()

name = input("Enter student name: ")
student.setName(name)

rollNumber = input("Enter student roll number: ")
student.setRollNumber(rollNumber)

print("Student Name is:", student.getName())
print("Student Roll Number is:", student.getRollNumber())