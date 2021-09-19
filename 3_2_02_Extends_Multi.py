'''
	클래스_다중 상속
'''

class A:
	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2
	def A1(self):
		print("{}/{}".format(self.a1, self.a2))

class B:
	def __init__(self, b1, b2):
		self.b1 = b1
		self.b2 = b2
	def B1(self):
		print("{}/{}".format(self.b1, self.b2))

class C(A, B):
	def __init__(self, a1, a2, b1, b2):
		A.__init__(self, a1, a2)
		B.__init__(self, b1, b2)

c1 = C("다", "중", "상", "속")

c1.A1()
c1.B1()