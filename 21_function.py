'''
	 함수
'''
def open_account():
	print("새로운 계좌가 생성되었습니다.")

open_account()
open_account()
open_account()

def deposit(balance, money):
	print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance + money))
	return balance + money

def withdraw(balance, money):
	if balance >= money:
		print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
		return balance - money
	else:
		print("출금이 거부되었습니다. 잔액은 {}원입니다.".format(balance))
		return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)