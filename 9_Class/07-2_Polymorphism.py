### 다형성(Polymorphism) ###


class Parent:
    def hello(self):
        return "I'm parent"


class Child(Parent):
    def hello(self):
        return "I'm first child"

    def hello2(self):
        return "I'm first child"


class Child2(Parent):
    def hello(self):
        return "I'm second child"


def greeting(person: Parent):  # person의 type이 Parent임을 힌트
    print(f"Greeting: {person.hello()}")


p = Parent()
c = Child()
c2 = Child2()

greeting(p)
greeting(c)
greeting(c2)


### 예제 2: 힌트는 힌트일 뿐!


def greeting2(person: Child):  # Child type으로 강제하지 않음
    print(f"Greeting2: {person.hello()}")


greeting2(p)  # 에러가 발생하지 않는다
greeting2(c)


class Stranger:
    def hello(self):
        return "I'm ananymous."

s = Stranger()
greeting2(s) # 심지어 힌트와 연간도 없음, 하지만 통과했죠