### 문화권 포멧 ###
import locale

print(locale.setlocale(locale.LC_ALL, "English_United States.1252"))
# locale.setlocale() : 숫자, 날짜, 통화 등에서 언어와 지역 특성을 반영하도록 세팅
# 영어(English), 미국(United States), Windows-1252(Western European language encoding)

conv = locale.localeconv()
x = 1234567.8
print(locale.format_string("%d", x, grouping=True))

print(
    locale.format_string(
        "%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x), grouping=True
    )
)
