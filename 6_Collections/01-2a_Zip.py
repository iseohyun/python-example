### zip함수를 이용한 2개 리스트 제어 ###

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}?  It is {1}.".format(q, a))



answers2 = ["alice", "waiting", "red"]
for q, a, b in zip(questions, answers, answers2):
    print("What is your {0}?  It is {1} and {2}.".format(q, a, b))