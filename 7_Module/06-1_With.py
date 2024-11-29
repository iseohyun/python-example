import datetime
### 안전한 코딩 ###
# f.close()를 호출하지 않아도 안전하게 시스템 자원을 반환

with open("7_Module/timestamp.txt", "a+", encoding="utf8") as f:
  f.write(f"{datetime.datetime.now()}\n")
  f.seek(0)
  print(f.read())
