from string import Template

t = Template("$village에서 $cause으로 10,000원을 기부해주셨습니다.")

print(t.substitute(village="거제", cause="지역나눔"))
print(t.safe_substitute(village="부산", cause="현장모금"))

try:
    print(t.substitute(village="거제"))
except Exception as err:
    print(err, "가 없습니다.")