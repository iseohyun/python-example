'''
	문자열처리
'''
python = "Python is Amazing"

print(python.lower())
print(python.upper())

print(python[0].isupper())
print(len(python))

print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.count("n"))
print(python.find("Java")) # 없으면 -1반환
print(python.index("Java")) #error 프로그램 종료
print("End") #실행안됨
