### 내장함수 ###
# https://docs.python.org/3/library/functions.html 참조

# 내장 변수(예: __name__) 제외한 호출(import)된 모듈 조회
print(f"1. Start >> {[item for item in dir() if not item.startswith("_")]}")

# 모듈을 호출하지 않고도 사용할 수 있는 함수 목록 조회
import builtins
print(f"\n2. build-in >> {[item for item in dir(builtins) if not item.startswith("_")]}")

import random

print(f"\n3. Add random >> {[item for item in dir() if not item.startswith("_")]}")

# random모듈에 속한 모든 항목으로 리스트 작성
print(f"\n4. In random >> {[item for item in dir(random) if not item.startswith("_")]}")
