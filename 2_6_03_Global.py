'''
	 지역변수와 전역변수
'''

gun = 10
def checkpoint(soldiers): # 경계근무
	global gun
	gun = gun - soldiers
	print("남은 총 : ", gun)

def checkpoint_ret(gun, soldiers):
	gun = gun + soldiers
	print("남은 총", gun)
	return gun

print("전체 총 : ", gun)
checkpoint(2)
print("전체 총 : ", gun)
gun = checkpoint_ret(gun, 2)
print("전체 총 : ", gun)