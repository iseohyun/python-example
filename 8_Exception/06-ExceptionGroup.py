### multiple exceptions ###
# 병령구조의 프로그램등에서 예외 발생시 바로 예외를 수행하기 보다, 우선 수행한 후, 한 번에 예외를 처리해야한다고 할 때, group으로 처리 할 수 있습니다.

def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 2, in <module>
#   |     f()
#   |     ~^^
#   |   File "<stdin>", line 2, in f
#   |     raise ExceptionGroup(
#   |     ...<12 lines>...
#   |     )
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
