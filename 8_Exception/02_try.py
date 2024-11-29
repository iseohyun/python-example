### 오류 처리: 오류 감지 및 동작  ###

try:
    a = 1 / 0  # "0으로 나눔 오류"발생
except ZeroDivisionError:
    print("에러: 0으로 나눌 수 없습니다.")
