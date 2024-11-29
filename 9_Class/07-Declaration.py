### Function defined ###


def f1(self, x, y):  # outside the class
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return "hello world"

    h = g

# f, g, h는 모두 C이 method이다. (f1은 아님)
obj = C()
print(obj.f(1, 2))
print(obj.g())
print(obj.h())
