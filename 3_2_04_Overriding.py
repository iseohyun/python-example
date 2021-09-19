'''
	클래스_오버라이딩
'''

class A:
	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2
	def show(self):
		print("{}/{}".format(self.a1, self.a2))

class B(A):
	def __init__(self, b1, b2):
		super().__init__(b1, b2)
	def show(self):
		print("{}/{}".format(self.a2, self.a1))
	def origin(self):
		super().show()

a1 = A("상", "속")
b1 = B("상", "속")

a1.show()
b1.show()
b1.origin()