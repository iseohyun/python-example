rainbow = ["Red", "Yellow", "Green"]
print(rainbow)  # ['Red', 'Yellow', 'Green']

rainbow += ["Blue", "Indigo"]
print(rainbow)  # ['Red', 'Yellow', 'Green', 'Blue', 'Indigo']

print(rainbow.index("Yellow"))  # 1

print(rainbow[1:4])  # ['Yellow', 'Green', 'Blue']

rainbow.append("Purple")
print(rainbow)  # ['Red', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

rainbow.insert(1, "Orange")
print(rainbow)  # ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

print(rainbow.pop())  # Purple
print(rainbow)  # ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo']

print(rainbow.pop())  # Indigo
print(rainbow)  # ['Red', 'Orange', 'Yellow', 'Green', 'Blue']

print(rainbow)
print(rainbow.count("Blue"))  # 1

rainbow[3] = "Gray"
print(rainbow)  # ['Red', 'Orange', 'Yellow', 'Gray', 'Blue']

rainbow.sort()
print(rainbow)  # ['Blue', 'Gray', 'Orange', 'Red', 'Yellow']

rainbow.reverse()
print(rainbow)  # ['Yellow', 'Red', 'Orange', 'Gray', 'Blue']

rainbow.clear()
print(rainbow)  # []
