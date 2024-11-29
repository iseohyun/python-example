### 코드예시 ###
# python.org 튜토리얼 코드를 복원: collections 모듈의 deque를 다음과 같이도 이용할 수 있다는 예시를 들면서...
from collections import deque

# 그래프 표현 (인접 리스트 방식)
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

# 목표 상태
goal = "F"


# 목표 상태를 확인하는 함수
def is_goal(node):
    return node == goal


# 가능한 이동(인접 노드)을 생성하는 함수
def gen_moves(node):
    return graph.get(node, [])


# BFS(너비 우선 탐색) 구현
def breadth_first_search(starting_node):
    unsearched = deque([starting_node])  # 탐색 대기열 초기화
    visited = set()  # 이미 방문한 노드 집합

    while unsearched:
        node = unsearched.popleft()  # 대기열에서 노드를 꺼냄
        print(f"Visiting: {node}")  # 현재 방문한 노드 출력

        if is_goal(node):  # 목표 상태인지 확인
            return f"Goal {node} found!"

        if node not in visited:  # 방문하지 않은 경우
            visited.add(node)  # 방문 표시
            for move in gen_moves(node):  # 인접 노드를 대기열에 추가
                if move not in visited:
                    unsearched.append(move)

    return "Goal not found."


# 시작 노드
starting_node = "A"

# 탐색 시작
result = breadth_first_search(starting_node)
print(result)
