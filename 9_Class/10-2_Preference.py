### 우선권 ###
# 중복되었을 때, 먼저 상속받은 것에 대해 수행한다.

class A:
    def __init__(self):
        print("A가 호출됨")


class B:
    def __init__(self):
        print("B가 호출됨")


class C(A, B):
    def __init__(self):
        super().__init__()


class D(B, A):
    def __init__(self):
        super().__init__()


c = C()  # A를 먼저 상속받음
d = D()  # B를 먼저 상속받음
