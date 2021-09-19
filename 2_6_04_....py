'''
	 가변함수
'''

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
	print("이름 : {}\t나이 : {}\t".format(name, age), end=">> ")
	print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Java", "C", "HTML", "SQL")
profile("김태호", 25, "kotlin", "C++", "javascript", "", "")

def profile(name, age, *language):
	print("이름 : {}\t나이 : {}\t".format(name, age), end = ">> ")
	for lang in language:
		print(lang, end=", ")
	print()

profile("김종국", 30, "Go", "python", "Java", "C", "HTML", "SQL")
profile("양세형", 35, "javascript", "C#")