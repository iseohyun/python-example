###	my package 1 ###


class pack1:
    def showMe(self, val):
        print("My package 1 : {}".format(val))


if __name__ == "__main__":
    print("\n직접 호출됨>>")
    pack = pack1()
    pack.showMe(1)
else:
    print(" - 외부에서 호출 됨")
