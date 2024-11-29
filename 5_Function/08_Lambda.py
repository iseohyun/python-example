###	람다: 이름없는 함수 ###
# 람다 함수는 함수의 축약형이다. 축약형을 사용하는 이유는...
#   1. 함수의 구조가 너무 간단하거나,
#   2. 함수가 반복적으로 호출되지 않고, 단 한 번 사용될 때


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))
