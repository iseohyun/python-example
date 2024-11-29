### 함수 내 감지 ###


def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print("에러 내용:", err)
