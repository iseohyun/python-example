### 파일 생성/읽기/쓰기 ###
#
# open('파일이름', '모드', encoding='코덱')
# 모드 : r(readonly[default]), w(writeonly, 파일 덮어씀), a(끝에 붙이기)
#   *   '+' (쓰기+읽기): r+: 앞에 추가(덮어쓰며), w+(싹다 지우고 앞부터), a+(뒤에 쓰기+읽기)
#   **  'b' (binary mode): i.e. rb, wb, ab
# 코덱(예): UTF-8, default(플랫폼 기본 설정)

import datetime

f = open("7_Module/timestamp.txt", "a+", encoding="utf8")

f.write(f"{datetime.datetime.now()}\n")
f.seek(0) # 읽기 커서를 처음으로 이동시킴
print(f.read())

f.close() # 중요: 시스템 자원을 반드시 반환해야 함
