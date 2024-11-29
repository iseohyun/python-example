### 내장 리스트 형 ###
from array import array

a = array("H", [4000, 10, 700, 22222])  # 'H'는 부호없는 2byte숫자를 의미(0~65,536)

print(sum(a))

print(a[1:3])
