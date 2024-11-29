### 피보나치 함수 ###


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b  # (a, b) = (b, a + b) 튜플 복사
