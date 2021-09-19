'''
	 print Format
'''
# 각 출력의 차이점은?
print("python"+"java")
print("python", "java")
print("python", "java", sep="/")

# 빈공간 만들어서 출력해보기
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
	#print(subject, score)
	print(subject.ljust(8), str(score).rjust(4), sep=":")

# 빈공간 0으로 채워서 출력하기 : 001, 002, 003 ...
for num in range(1,150,17):
	print("대기번호 : "+str(num).zfill(3))