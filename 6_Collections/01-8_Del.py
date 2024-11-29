### 리스트 내용 삭제 방법 ###

a = [i for i in range(6)]
print(a)  # [0, 1, 2, 3, 4, 5]

del a[0]
print(a)  # [1, 2, 3, 4, 5]

del a[2:4]
print(a)  # [1, 2, 5]

del a[:]
print(a)  # []
