### break/continue ###

for i in range(10):
    if i == 2:
        continue # 루프 중 이번 루틴만 건너 뜀
    if i == 5:
        break # 현재 루프를 종료
    print("%d 번째" % i)
