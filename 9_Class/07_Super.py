### Super ###


class Parent:
    data = "Parent" # Parent에 data가 있음


class Child(Parent):
    data = "Child" # Child에도 data가 있음
    
    def pdata(self):
        return super().data # Parent의 data를 참조


c = Child()
print(c.data) # 본인(Child)의 data가 호출
print(c.pdata()) # super()의 data가 호출
