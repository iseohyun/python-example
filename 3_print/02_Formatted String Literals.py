### print Format ###

print("{: >10}".format("*"))  # >: 우로정렬, 10: 10칸 확보
print("{: >10}".format("**"))
print("{: >10}".format("***"))
print("{: >10}".format(500))
print("{: >+10}".format(500))  # +: 기호표시
print("{: >+10}".format(-500))
print("{:_>+10}".format(-500))  # _:빈칸에 _로 채움
print("{:,}".format(1234567890))  # ,: 콤마(,)추가
print("{:+,}".format(1234567890))
print("{:^<+30,}".format(1234567890))  # < 좌료정렬, ^빈칸은 ^로 채움

print("'\n")
print("{}".format(5 / 7))
print("{:f}".format(5 / 7))  # float형식으로 출력(기본 double)
print("{:.2f}".format(5 / 7))  # .2 (소숫점2자리), f생략가능
print("{:.19f}".format(5 / 7))
print("{:*>+10.3f}".format(5 / 7))
# 10자리 확보하고 소수점 3자리까지 출력하는데, 기호 표시하고, 빈칸은 *로 채움

print("'\n")
num1 = 5 / 7
print(f"{num1:.2f}")
