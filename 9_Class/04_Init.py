### self ###
class MyClass:
    def __init__(self, i): # 초기화 할 수 있다. 생성시 반드시 호출된다.
        self.i = i

    def printi(self):
        print(self.i)


my1 = MyClass(777) # 객체 생성

my1.printi()

my1.i = 333

my1.printi()
