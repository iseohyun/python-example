### unpack: 입력인자를 분리하는 과정 ###


def unpack(*args):
    return args[1]


def unpack2(*args):
    for i in args:
        print(i, end=" ")


print(unpack("earth", "mars", "venus"))
unpack2("earth", "mars", "venus")
