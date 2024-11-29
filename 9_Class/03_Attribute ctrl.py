### self ###
class MyClass:
    i = 12345

    def seti(self, i):
        self.i = i

    def printi(self):
        print(self.i)


my1 = MyClass()

my1.printi()

my1.seti(99999)

my1.printi()
