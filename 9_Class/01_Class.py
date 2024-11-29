### Class: 객체 ###
# 객체는 attribute(속성)들과 method(함수)들로 이루어져 있다.
# 접근은 '클래스명.속성'또는 '클레스명.함수'와 같다.
# 모든 자료구조는 대문자로 시작한다.


class MyClass:
    i = 12345

    def f():
        print(f"MyClass")


MyClass.f()
print(MyClass.i)