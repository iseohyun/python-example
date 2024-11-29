import datetime

# 현재 요일 가져오기
current_day = datetime.datetime.now().strftime('%A')
print("Current day:", current_day)


# 요일을 숫자로 가져오기 (e.g., Sunday = 0, Saturday = 6)
day_number = datetime.datetime.now().strftime('%w')
print("Day number:", day_number)
