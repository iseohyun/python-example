### 함수에게 정보 전달하기 ###
def func1(arg1):
    print(f"Received data: {arg1}")


func1("information 1")
func1("information 2")


# 정보 2개 전달하기
def add(arg1, arg2):
    print(f"Data : {arg1}, {arg2}")


add(10, 20)
add(30, 50)
