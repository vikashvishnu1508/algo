class A1:
    a1 = "test1"

class A2:
    a2 = "test2"


class Student(A1, A2):
    def __init__(self):
        self.a1 = A1
        self.a2 = A2

studentObj = Student()
print(studentObj.a1)
print(studentObj.a2.a2)

