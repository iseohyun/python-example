'''
	 if
'''
weather = input("오늘 날씨는 어때요? : ")
if weather == "비" or weather == "눈":
	print("우산을 준비하세요")
elif weather == "미세먼지":
	print("마스크를 챙기세요")
else:
	print("준비물이 필요없어요.")