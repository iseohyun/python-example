### list함수를 이용한 제어 ###
"""
  list.append(x)  아이템 추가. a[len(a):] = [x]
  list.extend(iterable) a[len(a):] = iterable
  list.insert(i, x) 주어진 위치(i)에 항목(x)을 삽입.
  list.remove(x)  리스트에서 값이 x와 같은 첫 번째 항목을 삭제. 없으면 ValueError
  list.pop([i]) 주어진 위치(i)를 삭제, 생략시 마지막 아이템 삭제
  list.clear()  모든 리스트 내 아이템 삭제. del a[:]
  list.index(x[, start[, end]])   
    리스트에 있는 항목 중 값이 x 와 같은 첫 번째 것의 인덱스 반환. 없으면 ValueError.
  list.count(x) 리스트에서 x 가 등장하는 횟수.
  list.sort(*, key=None, reverse=False)  정렬, 정렬 기준과 규칙(오름차순)
  list.reverse()  리스트의 요소들을 거꾸로 배치
  list.copy() 리스트 복사. Similar to a[:].
"""
#         0         1        2       3         4       5        6
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))  # 2
print(fruits.index("banana"))  # 3

print(fruits.index("banana", 4))  # Find next banana starting at position 4

fruits.reverse()
print(fruits) # ["banana", "apple", "kiwi", "banana", "pear", "apple", "orange"]

fruits.append("grape")
print(fruits)
# ["banana", "apple", "kiwi", "banana", "pear", "apple", "orange", "grape"]

fruits.sort()
print(fruits)
# ["apple", "apple", "banana", "banana", "grape", "kiwi", "orange", "pear"]

print(fruits.pop()) # pear
