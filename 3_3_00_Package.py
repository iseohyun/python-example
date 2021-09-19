import myPackage.myPack1
pack = myPackage.myPack1.pack1()
pack.showMe(1)

from myPackage.myPack1 import pack1
pack = pack1()
pack.showMe(2)

from myPackage.myPack2 import *
pack = pack2()
pack.showMe2(3)