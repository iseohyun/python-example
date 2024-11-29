### 인터프리터가 읽을 수 있는 방식으로 출력 ###
import pprint

t = [[[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]]

pprint.pprint(t, width=30)
