vec = [-4, -2, 0, 2, 4]

print([x * 2 for x in vec])  # [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])  # [0, 2, 4]

# apply a function to all the elements
print([abs(x) for x in vec])  # [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
print([weapon.strip() for weapon in freshfruit])
# ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([elem for elem in vec]) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
