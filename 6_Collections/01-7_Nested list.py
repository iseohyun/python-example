### 이중(삼중, 사중) 리스트(또는 자료형) ###


matrix = [
    [1, 2, 3, 4], # row 0
    [5, 6, 7, 8], # row 1
    [9, 10, 11, 12], # row 2
]

print(matrix[1][1])

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


print(list(zip(*matrix)))  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
