### 이터레이터 ###
# __next__()를 정의하는 iterator객체를 반환
# next()를 통해, __next__()를 호출하지만,
# 남은 요소가 없을 때, stopIteration예외가 발생

s = 'abc'
it = iter(s)

print(next(it))
print(next(it))
print(next(it))
print(next(it))