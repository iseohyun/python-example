### 시스템 날짜 가져오기 ###

import datetime

# 현재 시간 가져오기
current_time = datetime.datetime.now()
print("Current time:", current_time)

# 날짜만
current_date = datetime.datetime.now().date()
print("Current date:", current_date)

# 시간만
current_time = datetime.datetime.now().time()
print("Current time:", current_time)
