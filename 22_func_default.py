'''
	 함수(기본값)
'''
def profile(name, age, main_lang):
	print("이름 : {}\t나이 :{}\t주 사용 언어: {}".\
		format(name, age, main_lang))

profile("유재석", 20, "자바")

def profile2(name, age=17, main_lang="파이썬"):
	print("이름 : {}\t나이 :{}\t주 사용 언어: {}".\
		format(name, age, main_lang))

profile2("김태호", 19)
profile2("박명수")