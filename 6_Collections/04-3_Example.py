cabinet = {3: "정도전", 100: "이방원"}
print(cabinet[3])  # 정도전
# print(cabinet.get(3)) # =같은 문법

# print(cabinet[5]) # 에러
print(cabinet.get(5))  # None
print(cabinet.get(5, "사용가능"))  # 사용가능

print(3 in cabinet)  # True
print(5 in cabinet)  # False

## key값은 문자열도 가능
cabinet = {"A-3": "황희", "B-100": "맹사성"}
print(cabinet)  # {'A-3': '황희', 'B-100': '맹사성'}
print(cabinet["A-3"])  # 황희

cabinet["A-3"] = "이숙번"
cabinet["C-20"] = "유정현"
print(cabinet)  # {'A-3': '이숙번', 'B-100': '맹사성', 'C-20': '유정현'}

del cabinet["A-3"]
print(cabinet)  # {'B-100': '맹사성', 'C-20': '유정현'}

print(cabinet.keys())  # dict_keys(['B-100', 'C-20'])
print(cabinet.values())  # dict_values(['맹사성', '유정현'])
print(cabinet.items())  # dict_items([('B-100', '맹사성'), ('C-20', '유정현')])

cabinet.clear()
print(cabinet)  # {}
