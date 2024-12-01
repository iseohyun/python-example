### Instance ###
# Class는 개념(설계)이고, Instance는 실제이다.
# 객체(자료구조) => 대문자 시작, 변수(인스턴스) => 소문자 시작


class MyClass:
    i = 12345

    def f(self):
        print(f"MyClass")


my1 = MyClass() # Instance 생성

my1.f()
print(my1.i)

# my1과 my2는 같은 설계도로 작성된, 서로다른 변수(저장공간)이다.
my2 = MyClass()
my2.i = 54321
print(f"my1.i: {my1.i}, my2.i: {my2.i}")