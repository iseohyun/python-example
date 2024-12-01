###	다중 상속: 중복 ###
# C에서 A, B를 상속받고, 둘 다 a 속성을 갖는 경우
# C는 2개의 a속성을 갖는 것이 아니라 하나의 a만 갖는다.

class A:
    def __init__(self, a):
        self.a = a

    def a1(self):
        print(f"{self.a}")

    def setA(self, a):
        self.a = a


class B:
    def __init__(self, a):
        self.a = a # 중복되었을 때, 하나의 저장공간으로 인식

    def b1(self): # method는 중복되지 않음
        print(f"{self.a}")


class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b) # B의 초기화가 늦게 이루어짐(덮어씀)


c1 = C("Class A", "Class B")

c1.a1() # Class B (덮어씀)
c1.b1()
c1.setA("Class C1") # Class A에서 씀
c1.b1() # Class B에서 읽음
