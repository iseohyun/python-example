import bisect

scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
bisect.insort(scores, (300, "ruby")) # 순서에 맞춰 중간에 들어감
print(scores)
