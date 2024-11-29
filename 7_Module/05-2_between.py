import datetime

# 특정한 날짜를 지정
past_date = datetime.date(2000, 1, 1)

# 오늘 날짜를 가져옴
today_date = datetime.date.today()

# 두 날짜간의 차이를 구함
difference_from_today = today_date - past_date
print("Days from past date to today:", difference_from_today.days)
