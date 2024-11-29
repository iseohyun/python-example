import datetime

# 날짜를 가져옴
current_date = datetime.datetime.now()

# 국제표준(ISO 8601 week number)에 의한 몇번째 주인지 확인
iso_year, iso_week, iso_weekday = current_date.isocalendar()

print(f"ISO Week Number for this year: {iso_week}")
