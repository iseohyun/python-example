'''
	변수 이해하기
'''

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age>=3

#==============================
print("우리집 "+ animal +" 이름은 "+ name +"예요")
print(name+"는 "+ str(age) +"살이며, "+hobby+"을 아주 좋아해요")
print(name+"는 어른일까요? "+ str(is_adult))

#==============================
#출력 비교해보기 - 띄어쓰기(' ')가 자동으로 삽입됨에 주의
print()
print("우리집 ", animal, " 이름은 ", name, "예요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? ", str(is_adult))