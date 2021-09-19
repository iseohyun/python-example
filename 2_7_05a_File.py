'''
	파일
'''
score_file = open("score.txt", "a", encoding="utf8")
score_file_r = open("score.txt", "r", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.write("코딩 : 100\n")

print(score_file_r.readline(), end="")
print(">>>")
print(score_file_r.read())


score_file.close()
score_file_r.close()
