### Match ###

val = 3 # 만약 val이 3이 아니었다면?
match val:
    case 1:
        print("first")
    case 2:
        print("second")
    case 3:
        print("third")
    case 4 | 5:
        print("fourth or fifth")
    case _:
        print("none of those")
