'''
	 함수(기본값)
'''

#1. 기본적인 함수의 모습
def profile(name, age, main_lang):
	print("이름 : {}\t나이 :{}\t주 사용 언어: {}".\
		format(name, age, main_lang))

profile("유재석", 20, "자바")

#2. 기본값(default)를 지정한 경우
def profile2(name, age=17, main_lang="파이썬"):
	print("이름 : {}\t나이 :{}\t주 사용 언어: {}".\
		format(name, age, main_lang))

#입력 인자를 명시하지 않으면, profile2의 default값이 자동으로 저장됩니다.
profile2("김태호", 19)
profile2("박명수")

# 키워드 값을 이용하면, 함수 호출 순서를 자유롭게 할 수 있습니다.
profile(name="유재석", main_lang="파이썬", age=21)
profile(main_lang="자바", age=22, name="김태호")