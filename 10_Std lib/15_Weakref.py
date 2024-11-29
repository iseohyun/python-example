### 약한 참조 ###
# 모듈 참조를 만들지 않고, 추적할 수 있는 도구를 제공, 단, 비용이 많이 듬

import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)  # Step 1. 원본 작성
d = weakref.WeakValueDictionary()  # Step 2. 약한 참조 생성
d["primary"] = a  # Step 3. 연결

print(d["primary"])

del a  # Step 4. 원본(reference)를 삭제

gc.collect()  # Step 5. garbage collection(메모리에서 제거)

print(d["primary"])  # Step 6. 약한참조 조회 - ERROR: 존재하지않음

# 참고 (__repr__ VS __str__)
# __repr__ : REPResentation(표현)을 반환 -> 디버깅, 재생성에 유리
# __str__ : STRing(문자열)을 반환 -> 사용자 친화적, 가독성 위주
