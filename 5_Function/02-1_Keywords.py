### positional arguments vs. keyword arguments ###
# 함수에게 정보를 전달할 때, 정보가 2개 이상이라면...
# 순번(positional)을 기반으로 서로 구분하거나, 태그(keyword)를 통해 구분할 수 있다.


def func1(x=1, y=2, z=3):
    """
    이 함수는 태그(keyword)가 없다면, 순서대로 x, y, z로 간주합니다.
    만약 입력되지 않는다면 각각 1, 2, 3을 입력한 것으로 간주합니다.
    """
    print(x, y, z)


func1(8, 9, 10)  # 8 9 10 -> 지정된 순서대로 입력
func1()  # 1 2 3 -> 기본값으로 설정됨
func1(8, 9)  # 8 9 3 -> 순서대로 x, y에 입력
func1(y=8, z=9)  # 1 8 9 -> y, z에 입력
func1(z=10, x=10)  # 10 2 10 -> z부터 입력해도 ok
