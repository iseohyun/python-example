# sys 모듈은 stdin, stdout, stderr attribute도 가지고 있음. stdout이 리디렉트 되었을 때도 볼 수 있는 경고, 에러 메시지를 출력
import sys

sys.stderr.write("Warning, log file not found starting a new one\n")

sys.exit() # 프로그램 종료

print("running") # 출력되지 않음
