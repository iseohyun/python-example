### 클래스_상속 ###


# 부모 클래스: Parent
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"I am {self.name}, a Parent."


# 자식 클래스: Child
class Child(Parent):
    def greet(self):
        return f"I am {self.name}, a Child."


# 객체 생성
parent_instance = Parent("Alice")
child_instance = Child("Bob")

# 동작 확인
print(parent_instance.greet())  # I am Alice, a Parent.
print(child_instance.greet())  # I am Bob, a Child.
