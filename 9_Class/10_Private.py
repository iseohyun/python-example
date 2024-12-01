### 비공개 변수 ###


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # sub클래스에서 재정의 되지 않도록 보장


class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


mapping = Mapping([1, 2, 3])
print("초기화 결과:", mapping.items_list)

mapping_subclass = MappingSubclass([4, 5, 6])
print("초기화 결과(sub):", mapping_subclass.items_list)  # [4, 5, 6]

keys = ["key1", "key2", "key3"]
values = ["value1", "value2", "value3"]
mapping_subclass.update(keys, values)
print("업데이트(sub):", mapping_subclass.items_list)
# [4, 5, 6, ('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]

mapping.update([7, 8, 9])
print("업데이트:", mapping.items_list)  # [1, 2, 3, 7, 8, 9]
