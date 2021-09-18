'''
	리스트
'''

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

subway.sort()
print(subway)

subway.reverse()
print(subway)

mix_list = ["abc", 1, True]
print(mix_list)
mix_list.extend(subway)
print(mix_list)

subway.clear()
print(subway)