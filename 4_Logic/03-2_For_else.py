### for 반복문 ###

for i in range(5):
    print(i, end=" ")
else:
    print("for else #1") # 수행 됩니다.

for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("for else #2") # 수행되지 않습니다.
