### 연산 기호 이해(암기)하기 ###

print("#1. 산술 연산")
print("3 +  2 = ", 3 + 2)  # 5
print("3 -  2 = ", 3 - 2)  # 1
print("3 *  2 = ", 3 * 2)
print("3 /  2 = ", 3 / 2)
print("7 // 2 = ", 7 // 2)
print("7 %  2 = ", 7 % 2)  # 나머지
print("3 ** 2 = ", 3**2)

print("\n#2. 비교 연산")
print("3 == 3    : ", 3 == 3)
print("3 != 2    : ", 3 != 2)
print("5 > 3     : ", 5 > 3)
print("5 < 3     : ", 5 < 3)
print("5 >= 3    : ", 5 >= 3)
print("5 <= 3    : ", 5 <= 3)
print("3 < 4 < 5 : ", 3 < 4 < 5)  # 파이선 문법: 3<4 참, 4<5 참, 결과: 참
print("3 < 4 < 1 : ", 3 < 4 < 1)  # 3<4 참, 4<1 거짓, 결과: 거짓

print("\n#3. 논리 연산")
print("True and False =", True and False)
print("True or  False =", True or False)
print("not True       =", not True)

a = 0b1100
b = 0b1010
print("\n#4. 비트 연산 연산")
print(f"{a:b} & {b:b} = {a&b:04b}")
print(f"{a:b} | {b:b} = {a|b:04b}")
print(f"{a:b} ^ {b:b} = {a^b:04b}")
print(f"!{a:b}       = {~a&0b1111:04b}") # 2의 보수 출력 문제, 마스크 00001111
print(f"{0b0110:04b}<<1     = {0b0110<<1:04b}")
print(f"{0b0110:04b}>>1     = {0b0110>>1:04b}")
