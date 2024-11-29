import fibo  # 모듈을 불러옵니다. 모듈의 이름은 fibo입니다.

fibo.fib(1000)  # fibo모듈의 fib함수를 수행합니다.


# fib()과 fib2()의 차이점은 콘솔에 직접 출력하는가(1)와 list를 반환하는가(2)입니다.
list = fibo.fib2(100)
print(list)  # fib2()에서 반환한 list를 출력합니다.

print(fibo.__name__)  # 모듈의 이름(파일명)을 출력

fib = fibo.fib  # fibo모듈의 fib함수를 지역함수(로컬)로 대입할 수 있습니다.
fib(500)