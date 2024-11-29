import threading
import time

def print_numbers(name, start, end):
    """주어진 범위의 숫자를 출력하는 함수"""
    for i in range(start, end):
        print(f"{name}: {i}")
        time.sleep(0.1)  # 0.1초 대기 (시뮬레이션용)

# 스레드 생성
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1, 6))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 6, 11))

# 스레드 시작
thread1.start()
thread2.start()

# 메인 스레드가 두 스레드가 끝날 때까지 기다림
thread1.join()
thread2.join()

print("All threads have finished execution.")
