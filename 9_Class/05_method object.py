### method object ###
class MyClass:
    i = 12345

    def __init__(self, i):
        self.i = i

    def printi(self):
        print(self.i)


my1 = MyClass(777)

mo = my1.printi  # method object 생성

mo()

my1.i = 99999

mo()
