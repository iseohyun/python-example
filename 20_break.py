'''
	 break/continue
'''
absent = [2, 5]
no_book = [7]

for student in range(1,11):
	if student in absent:
		continue
	elif student in no_book:
		print("{}, 교무실로 따라와".format(student))
		break
	print("{}, 책을 읽어보렴.".format(student))
	