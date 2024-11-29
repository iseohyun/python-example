### test를 자동으로 수행해준다 ###
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    >>> print(average([59, 30, 70]))
    53.0
    """
    return sum(values) / len(values)


import doctest

resault = doctest.testmod()  # automatically validate the embedded tests
print(resault)

# __document__에 기록된 테스트케이스를 수행해줌
# (20+30+70)/3 = 40...
