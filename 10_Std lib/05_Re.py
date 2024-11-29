import re

# \b: 단어시작, f: f가 들어감, []: 패턴, a-z:a~z중 하나의 문자, *:0개 이상
# => f로 시작하면서 a~z의 문자가 연속으로 0개 이상인 단어
r = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(r)

# ()로 묶인 부분을 순서대로 \1, \2 ... 로 지정
# the the를 the로 바꿈
r = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")
print(r)
