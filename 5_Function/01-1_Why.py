### 함수는 왜 정보를 주고 받아야하는가? ###

# 이유1. 함수 안에서 취급하는 정보와 밖에서 취급하는 정보가 서로 다르다.
#        그러므로 함수 밖의 정보를 가져다주는 역할이 필요
# 지역변수와 전역변수는 충돌을 방지하기 위한 설계
# 그렇지 않으면, 1. 코더는 프로그램내 모든 변수를 기억해야 함
#                2. 함수가 많아질수록 변수명은 길어지고, 기억하기 어려워짐(악순환)

# 지역변수를 설명하는 예시:
def func1():
    var = 2  # 지역변수: 국지적인 영역(예: 함수 안)에서만 효력
    print(f"func1 : {var}")


var = 1  # 전역변수: 모든 영역에서 효력
print(f"step 1: {var}")
func1()
print(f"step 2: {var}")
func1()
