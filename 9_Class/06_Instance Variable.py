### shared by all instance ###
class Dog:
    kind = "canine"  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog("Fido")
e = Dog("Buddy")
print(f"Name> d: {d.name}, e: {e.name}")  # unique to d, e
print(f"Kind(no change)  > d: {d.kind:6}, e: {e.kind}")  # shared by all dogs

Dog.kind = "Hound"
print(f"Dog.kind = Hound > d: {d.kind:6}, e: {e.kind}")
# 개별 어트리뷰트가 있다면, 개별 어트리뷰트를 먼저 조회한다.

d.kind = "pooch"
print(f"d.kind = pooch   > d: {d.kind:6}, e: {e.kind}")

Dog.kind = "Furry"
print(f"Dog.kind = Furry > d: {d.kind:6}, e: {e.kind}")
