### scope : 유효성 범위 ###

# spam(global) <== global(최상위 단계)
#   spam(in scope_test) <== non_local(상위단계)
#     spam(in do_local)

# 함수가 호출 될 때, 그 위치에서 유효한 spam이 호출.
# 단, 키워드(global, non_local)가 있을 때, 해당 키워드를 반영


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
