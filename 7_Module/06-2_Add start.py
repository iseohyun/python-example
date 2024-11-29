### pythom에서 파일 앞에 추가하는 기능은 아직 지원하지 않음

import datetime

# 새로 추가할 내용
new_content = f"{datetime.datetime.now()}\n"

# 파일 이름 정의
file_path = "7_Module/timestamp.txt"

# 기존 내용을 읽어오고 새로운 내용을 맨 앞에 추가
with open(file_path, "r+", encoding="utf8") as f:
    # 기존 내용 읽기
    existing_content = f.read()
    # 파일 포인터를 맨 앞으로 이동
    f.seek(0)
    # 새로운 내용 + 기존 내용 쓰기
    f.write(new_content + existing_content)
