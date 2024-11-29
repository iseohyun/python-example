###	어노테이션 : 함수의 성질(특징)을 참조(불러오는) 방법 ###


def f(ham: str, eggs: str = "eggs") -> str:
    """
        이 함수는 2개의 인자를 받는데, 그 이름은 각각 ham, eggs이다.
        ham과 eggs 모두 문자열(string)만 입력 받을 수 있고,
        반환값도 반드시 문자열로 반환한다.
    """
    print("Annotations:", f.__annotations__)


f("spam")
