### 리스트: 단순 나열형 데이터 집합 ###


#         0         1        2       3         4       5        6
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits) # 전체 읽기

print(fruits[0]) # 부분 읽기(0)

print(fruits[6]) # 부분 읽기(6)

fruits[3] = "tomato" # 쓰기(3)

print(fruits) # 확인: [3] "banana" -> "tomato"
