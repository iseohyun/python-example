### 성능 측정 ###
from timeit import Timer

# Timer("동작 코드", "초기화")
print(Timer("t=a; a=b; b=t", "a=1; b=2").timeit())  # 1번 임시변수

print(Timer("a,b = b,a", "a=1; b=2").timeit())  # 2번 튜플 언패킹(승)

# 1번과 2번은 모두 a <-> b swap(교환)방법으로,
# 임시변수를 사용한 방법과 튜플 언패킹을 사용한 방법의 성능차이를 본다.
