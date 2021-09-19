'''
	Exception
'''
class BigNumberError(Exception):
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		return self.msg

print("#1")
try:
	num1 = int(input("1자리 숫자를 입력하세요: ")) #문자를 입력하면 어떠한 일이 일어나나요? 2자리 숫자를 입력하면?
	if num1 >= 10:
		raise BigNumberError("2자리 숫자 입니다.")# 2자리 숫자가 입력되면 강제로 예외 발생
	num1 = 1/0;
except ValueError:
	print("에러! 잘못된 값을 입력하였습니다.")
except BigNumberError as err:
	print(err)
except ZeroDivisionError as err:
	print(err)
finally:
	print("finally : 에러여부와 상관없이 실행")

#2
print("\n#2")
try:
	num2 = []
	num2[0] = 1;
except Exception as err:
	print("에러 내용 : {}".format(err))

print("정상적으로 프로그램이 종료되었습니다.")