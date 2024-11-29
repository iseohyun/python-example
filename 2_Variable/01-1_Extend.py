### Python에서 지원하는 여러가지 숫자 표현 방식 - 진법, 지수, 복소수 ###

## Exponent((멱)지수)
x = 2.5e4  # 25000
y = 3.0e-2  # 0.03
print("결과 =", x * y)

## Formation(진법)
num1 = 0xF  # 0b1111 = 16
num2 = 0b1110  # 15
print("16진수 0xff =", num1)
print("2진수 0b101010 =", num2)

## complex number(복소수)
complex_num1 = 3 + 4j
complex_num2 = 2 - 1j
print("복소수 덧셈 =", complex_num1 + complex_num2)
print("복소수 곱셈 =", complex_num1 * complex_num2)
