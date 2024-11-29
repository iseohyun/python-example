class AppError(Exception):
    """기본 애플리케이션 에러"""

    def __init__(self, message, code=500):
        super().__init__(message)
        self.code = code


class DatabaseError(AppError):
    """데이터베이스 관련 에러"""

    def __init__(self, message, query=None):
        super().__init__(message, code=500)
        self.query = query


# 사용 예시
try:
    raise DatabaseError("DB 연결 실패", query="SELECT * FROM users")
except DatabaseError as e:
    print(f"에러: {e}, 코드: {e.code}, 쿼리: {e.query}")
