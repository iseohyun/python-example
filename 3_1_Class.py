'''
	클래스
'''

class Unit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print("{} 유닛이 생성되었습니다.".format(self.name))
		print("체력 {}, 공격력 {}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
tank.siegemode = True

print("유닛 이름 : {}, 체력 : {}, 공격력 : {}".format(tank.name, tank.hp, tank.damage))
if(tank.siegemode == True):
	print("시즈모드가 연구 되었습니다.")

#if(marine1.siegemode == True): # 오류발생
	print("시즈모드가 연구 되었습니다.")