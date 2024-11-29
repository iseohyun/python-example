### add_note ###
# 에러가 발생한 후에, 정보를 추가할 수있습니다.

try:
    raise TypeError("bad type")
except Exception as e:
    e.add_note("Add some information")
    e.add_note("Add some more information")
    raise
