###	다중 상속 ###


class A:
    def __init__(self, a):
        self.a = a

    def a1(self):
        print(f"{self.a}")


class B:
    def __init__(self, b):
        self.b = b

    def b1(self):
        print(f"{self.b}")


class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)


c1 = C("Class A", "Class B")

c1.a1()
c1.b1()
