from decimal import *
# decimal은 유효자리에 대한 연산을 올바르게 해준다.


print(Decimal("1.00") % Decimal(".10"))
print(1.00 % 0.10)
# 1을 0.1로 나눈 나머지는 0이다.

# 기본적으로 주어지는 sum()은 보정을 하기 때문에 단순 연산을 위한 sum제작
def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(sum([Decimal("0.1")] * 10) == Decimal("1.0"))
print(sum([0.1] * 10) == 1)
# 0.1을 10번 더하면 1이다.

getcontext().prec = 36 # 소수점 36자리
gap = Decimal(1) / Decimal(7)
print(gap, f"({len(str(gap))})")



# 번외: 기본적으로 주어지는 sum은 보정을 한다.(위 함수를 지운 후 실행ㄱㄱ)

print(sum([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]) == 1.0) #true
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0) #false
