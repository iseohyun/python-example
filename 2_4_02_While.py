'''
	 while
'''
customer = "토르"
index = 5
while index >= 1:
	print(f"{customer}님, 커피가 준비되었습니다. : {index}")
	index -= 1

person = ""
while person != "토르":
	print("{}님, 커피가 준비되었습니다.".format(customer))
	person = input("이름이 어떻게 되세요? : ")