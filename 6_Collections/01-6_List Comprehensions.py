### 리스트 자동 생성의 기술 ###


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

comb = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(comb)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
