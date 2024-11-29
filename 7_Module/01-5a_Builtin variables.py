""" 이 문서는,
    내장 변수(built-in variables)을 설명하기 위한 파일 """

import myPackage


# 1. 실행된 파일 감별
print(f"[1] {__name__}")  # "__main__" (직접 실행 시)

# 2. 파일의 위치 감별
print(f"[2] ...{str(__file__)[-60:]}")  # 실행 파일의 "디렉토리 + 파일명"

# 3. 문서 설명서 조회(있다면...)
print(f"[3] {__doc__}")  # "이 문서는, ... "

# 4. 현재 모듈
print(f"[4] this file: {__package__} / myPackage: {myPackage.__package__} ")  # "None": 최상위 모듈

# 5. 변수나 함수의 타입힌트
def func1(name: str, age: int) -> str:
    pass


print(f"[5] {func1.__annotations__}")


# 6. 내장함수 abs와 동일한 이름의 함수를 재정의
def abs(num):
    return num + 10


print(f"[6] abs(-4): {abs(-4)}, built-ins(-4): {__builtins__.abs(-4)}")  # 6

# 7. 업로드한 로더 객체 정보
print(f"[7] {__loader__}")  # <_frozen_importlib_external.SourceFileLoader object at ~

# 8. 모듈의 메타 데이타
print(f"[7] {str(myPackage.__spec__)[:60]}...")  # ModuleSpec(name='__main__', ...)

# 9. 캐시 정보를 조회
print(f"[9] ...{str(myPackage.__cached__)[-60:]}")

# 10. 현재 디버그 모드인지
print(f"[10] {__debug__}")
