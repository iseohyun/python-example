### 데이터 클레스: 단순 정보 저장용 객체 ###
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


john = Employee("john", "computer lab", 1000)
print(john.dept)
print(john.salary)
