### 세트, 집합(set): 중첩을 인정하지 않는 집합 ###


basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # {"orange", "banana", "pear", "apple"} - 중복된 것 삭제

print("orange" in basket)  # True - fast membership testing
print("crabgrass" in basket)  # False

# Demonstrate set operations on unique letters from two words
a = set("abracadabra")
b = set("alacazam")
print(a)  # {'b', 'c', 'r', 'a', 'd'}
print(b)  # {'c', 'z', 'a', 'l', 'm'}

print(a - b)  # {'b', 'r', 'd'} = 그룹A에만 있음

print(a | b)  # {'b', 'c', 'r', 'z', 'a', 'l', 'd', 'm'} = 합집합

print(a & b)  # {'c', 'a'} = 교집합

print(a ^ b)  # {'b', 'm', 'd', 'r', 'z', 'l'} = 합집합 - 교집합
