'''
	with
'''

with open("study.txt", "w", encoding="utf8") as study_file:
	study_file.write("파이선을 공부하고 있습니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
	print(study_file.read())