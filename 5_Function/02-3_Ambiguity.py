### 모호함 ###
# foo함수와 bar함수에는 '/'의 차이점이 있습니다. 이는 name을 postion only로 사용할지 차이점이 있습니다.


def foo(name, /, **kwds):  # '/' 문자로 name의 성격을 pos로 강제
    return "name" in kwds  # name은 kwds의 name임이 확실합니다.


def bar(name, **kwds):
    return "name" in kwds  # kwds의 name인지, bar arg의 name인지???


ret = foo(1, **{"name": 2})
print(ret)

ret = bar(1, **{"name": 2})  # TypeError: bar()...
