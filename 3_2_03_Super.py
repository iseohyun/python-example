'''
	Super
'''

class A:
	def __init__(self):
		print("Call A")

class B:
	def __init__(self):
		print("Call B")

class C(A, B):
	def __init__(self):
		super().__init__()

class D(B, A):
	def __init__(self):
		super().__init__()

c = C()
d = D()