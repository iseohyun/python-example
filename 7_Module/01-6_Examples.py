import min_max #1 일반적인 import예제
print("#1") 

min_max.PrintMax(1, 2)
min_max.PrintMax(2, 1)

import min_max as m #2 모듈명을 min_max에서 m으로 변경했을 때
print("\n#2")

m.PrintMax(3, 4)

from min_max import PrintMin #3 min_max의 PrintMin만 호출했을 때
print("\n#3")

PrintMin(5, 6)
# PrintMax(5, 6)

from min_max import * #3 모든 min_max의 함수를 호출 했을 때

PrintMax(5, 6)

from min_max import PrintMin as min #3 PrintMin의 이름을 min으로 변경했을 때

min(9, 10)
