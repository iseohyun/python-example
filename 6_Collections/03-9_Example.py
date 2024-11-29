mySet = {1, 2, 3, 3, 3}
print(mySet)  # {1, 2, 3}

java = {"정도전", "이방원", "남은"}
python = set(["하륜", "이방원"])

print(java & python)  # {'이방원'}
# print(java.intersection(python)) # 같은 동작

print(java | python)  # {'남은', '이방원', '하륜', '정도전'}
# print(java.union(python)) # 같은 동작

print(java - python)  # {'남은', '정도전'}
# print(java.difference(python)) # 같은 동작

python.add("이숙번")
print(python)  # {'이숙번', '하륜', '이방원'}

# java.remove("이숙번") # keyError: '이숙번'
java.remove("남은")  # {'이방원', '정도전'}
print(java)
