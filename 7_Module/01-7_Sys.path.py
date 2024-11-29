# 모듈 검색 경로
#
# 1. sys.builtin_module_names를 검색한다.
# 2. 현재 디렉터리를 검색한다.
# 3. PYTHONPATH (환경변수, 유저와 프로그램이 등록한 검색할 디렉터리 목록)
# 4. installation-dependent default (site-packages directory)

import sys

print(f"Mudule Names: {sys.builtin_module_names}")

for path in sys.path:
    print(path)
