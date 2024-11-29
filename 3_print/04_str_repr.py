###	str() vs. repr() ###

# 입력받은 내용 123과 '123'은 전혀 다릅니다.
# 123 + 1 = 124이고, '123' + 1 = '1231'입니다.
# 숫자로 입력 받았다고 하더라도 그것이 (예를들어) 주소라면, 문자열로 인식해야합니다.
# str() 함수는 전달받은 내용이 완벽하게 string으로 사용될 수 있도록 변환합니다.

str_num = str(123)
print(str_num)

# repr() 함수는 인터프리터에 의해 읽힐 수있는 형태로 만들어줍니다.
# 인터프리터는 컴퓨터 해석기라고 할 수 있습니다.

str_string = str("hello")
repr_string = repr("hello")
print(str_string)
print(repr_string)
