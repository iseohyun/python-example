'''
	import
'''
print("#1")
import module
module.PrintMax(1, 2)
module.PrintMax(2, 1)

print("\n#2")
import module as m
m.PrintMax(3, 4)

print("\n#3")
from module import PrintMin
PrintMin(5, 6)
#PrintMax(5, 6)

from module import *
PrintMax(5, 6)

from module import PrintMin as min
min(9, 10)
