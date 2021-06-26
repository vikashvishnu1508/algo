class A(object):
    def __init__(self) -> None:
        print("in A")
        super().__init__()

class A1(object):
    def __init__(self) -> None:
        print("in A1")
        super().__init__()


class B(A):
    def __init__(self) -> None:
        print("in B")
        super().__init__()

class C(A1):
    def __init__(self) -> None:
        print("in C")
        super().__init__()

class D(B, C):
    def __init__(self) -> None:
        print("in D")
        super().__init__()

d = D()
print(d)