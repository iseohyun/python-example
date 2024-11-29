### 반복문을 이용한 제어 ###

#         0         1        2       3         4       5        6
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

for fruit in fruits:
    print(fruit, end=", ")
print()

for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)
