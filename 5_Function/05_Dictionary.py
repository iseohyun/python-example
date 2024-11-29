### diction 자료형을 인자로 전달하는 방법 ###


def search(index="name", **dict):
    print(dict[index])


dict = {"name": "광해군", "year": 1592}
search(**dict)
search("year", **dict)
