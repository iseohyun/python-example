### 클래스_오버라이딩 ###
# 같은 이름의 속성과 메서드를 가질 수 있다. 호출되는 기준이되지만, 사라지는 것은 아니다.

class Parent:
	def show(self):
		print(__class__)

class Child(Parent):
	def show(self):
		print(__class__)
	def show_super(self):
		print(__class__, end=" -> ")
		super().show()

p = Parent()
c = Child()

p.show()
c.show()
c.show_super()