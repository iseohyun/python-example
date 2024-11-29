### Dictionary: key(색인)과 value(내용)으로 이루어진 자료형 ###


tel = {"jack": 4098, "sape": 4139}  # jack과 sape의 전화번호를 등록
tel["guido"] = 4127  # guido의 전화번호를 등록

print(tel)  # 출력: {"jack": 4098, "sape": 4139, "guido": 4127}
print(tel["jack"])  # 출력: 4098

del tel["sape"]  # sape의 전화번호를 삭제

tel["irv"] = 4127  # irv의 전화번호를 등록
print(tel)  # 출력: {"jack": 4098, "guido": 4127, "irv": 4127}
print(list(tel))  # 출력: ["jack", "guido", "irv"]

tel = sorted(tel)  # 정렬(오름차순)
print(tel)  # 출력: ["guido", "irv", "jack"]

print("guido" in tel)  # 출력: True
print("jack" not in tel)  # 출력: False
