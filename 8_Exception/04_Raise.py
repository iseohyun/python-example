### 오류 고의 발생 ###
# 오류 발생을 설계자가 미리 감지 할 수 있다면, 현재 상태의 정보를 담아 바로 오류 처리 함수로 이동 할 수 있다.

try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(inst)
