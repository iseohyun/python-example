### 와일드 카드(*) 검색이 가능 ###

import glob

files = glob.glob("*")
for file in files:
  print(file)
