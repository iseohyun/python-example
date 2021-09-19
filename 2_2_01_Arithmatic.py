'''
	연산 이해하기
'''
print("#1. 단순연산")
print(1+1)
print(3-2)
print(5*2)
print(7/3)		#파이선 문법 - 일반적으로 7/3은 몫만 출력이되는데, 파이선은 실수로 간주함

print("#2. 특징적인 연산")
print(2**3)     # 지수승 2^3
print(5%3)      # 나머지
print(10%3)
print(5//3)     # 몫(정수) - 파이선은 몫을 구하기 위한 연산자가 추가로 필요함
print(10//3)

print("#3. 비교 연산")
print(10 > 3)
print(4 >= 7)
print(1 == 3)   # 주의! =가 2개
print(1 != 3)
print(3+4 == 7)
print(3<4<5)	# 파이선 문법
print(3<4<1)

print("#4. 논리 연산")
print(True and True)
print(True & True)
print((1>3) or (3<4))
print((1>3) | (3<4))