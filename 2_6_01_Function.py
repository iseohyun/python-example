'''
	 함수
'''

#함수는 정의부와 호출부로 이루어져 있습니다.
#정의부 : 정의만 되어 있고, 실제로 구동이 되지 않기 때문에 아무런 일도 일어나지 않습니다.
def open_account():
	print("새로운 계좌가 생성되었습니다.")

#호출부 : 정의가 되어 있는 함수를 호출하는 기능입니다. (이미 정의되어 있어야 합니다.)
#여러번 호출이 가능합니다.
open_account()
open_account()
open_account()

def deposit(balance, money):
	print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance + money))
	return balance + money

balance = 0
#호출되는 인자 값은, 순서대로 대응이 됩니다.
balance = deposit(balance, 1000)

def withdraw(balance, money):
	if balance >= money:
		print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
		return balance - money
	else:
		print("출금이 거부되었습니다. 잔액은 {}원입니다.".format(balance))
		return balance

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)