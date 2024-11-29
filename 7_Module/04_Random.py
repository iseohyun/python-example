### 랜덤(난수) 연산 ###

from random import *

print(random())  # 난수 생성(0 ~ 1사이의 실수 생성)

print(int(random() * 10))  # 0~9까지 정수
print(int(random() * 10 + 1))  # 1~10까지 정수

print(randrange(1, 10))  # 1 <= x < 10
print(randrange(1, 10, 2))  # 1 <= x < 10, 홀수만
print(randint(1, 10))  # 1 <= x <= 10
