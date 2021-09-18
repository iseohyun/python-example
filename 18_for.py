'''
	 for
'''
for waiting_no in [1, 2, 3, 4, 5]:
	print(f"대기번호 : {waiting_no}")

print("")
for waiting_no in range(5):
	print(f"대기번호 : {waiting_no}")

print("")
starbuck = ["아이언맨", "토르", "아엠 그루트"]
for customer in starbuck:
	print(f"{customer}님 커피가 준비되었습니다.")

students = [1,2,3,4,5]
print(students)
students = [ i+100  for i in students ]
print(students)

#print("")
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)
students = [len(i) for i in students]
print(students)