###	가변함수: 입력값의 갯수가 미확정인 함수 ###


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus", "mercury", "jupiter"))

print(concat("earth", "mars", "venus", sep=", "))
