class Student:
    def __init__(self, a1, *args):
        self.a1 = a1
        print("try a1 = ", a1)
        print("try = ", *args)

stu = Student("t1")
stu2 = Student("t2", "t3")
