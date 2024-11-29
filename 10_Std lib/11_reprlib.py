### 인터프리터가 읽을 수 있는 방식으로 출력 ###
import reprlib

print(set("supercalifragilisticexpialidocious"))
print(reprlib.repr(set("supercalifragilisticexpialidocious")))
