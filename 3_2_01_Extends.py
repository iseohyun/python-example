'''
	클래스_상속
'''

class Unit:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

class AttackUnit(Unit):
	def __init__(self, name, hp, damage):
		Unit.__init__(self, name, hp)
		self.damage = damage
	def Attact(self, location):
		print("{0}가 {1}로 공격 작전을 수행합니다.[{2}/{2}] > {3}".format(self.name, location, self.hp, self.damage))

marine = AttackUnit("마린", 40, 5)
tank = AttackUnit("탱크", 150, 35)

marine.Attact("1시")
tank.Attact("3시")