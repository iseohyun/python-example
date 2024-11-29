### 출력 포멧 ###

# 방법 1: printf style(old fassion)
print("나는 %d살 입니다." % 20)
print("나는 %s를 좋아합니다." % "사과")
print("나는 %d살 이고, %s를 좋아합니다." % (25, "사과"))
print("\n")

# 방법 2: str.format()
print("나는 {}살 입니다.".format(20))
print("나는 {}살 이고, {}를 좋아합니다.".format(25, "복숭아"))

print("나는 {0}살 이고, {1}를 좋아합니다.".format(25, "복숭아"))
print("나는 {1}살 이고, {0}를 좋아합니다.".format(25, "복숭아"))
print("나는 {0}살 이고, {0}를 좋아합니다.".format(25, "복숭아"))

print("나는 {age}살 이고, {like}를 좋아합니다.".format(age=30, like="호두"))
print("나는 {age}살 이고, {like}를 좋아합니다.".format(like="호두", age=30))
print("\n")

# 방법 3: f-string
age = 40
like = "수박"
print(f"나는 {age}살 이고, {like}를 좋아합니다.")
