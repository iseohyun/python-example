file_path = "7_Module/timestamp.txt"

# 기존 내용을 읽어오고 새로운 내용을 맨 앞에 추가
with open(file_path, "r+", encoding="utf8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i:3}: {line}", end="")