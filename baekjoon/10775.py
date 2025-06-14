# G개의 게이트가 있으며 각각은 1에서 G까지의 번호를
# P개의 비행기가 순서대로 도착할 예정
# i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹
# 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄
# 가장 많은 비행기를 공항에 도킹시킬때 최대 갯수는?

#그리디 일단 먼저 앞부터 채우는 경우도 안됨
# 7 7 1 인상황에서 앞부터 채우면 1이 들어갈 수 없음
# 1 7 7 로 게이트를 배치하면 풀 수 있음
# 그리디로 최대부터 채우면서 작은 것으로 줄이면?
# 100000 * 100000

"""
import sys

input = sys.stdin.readline

g = int(input())
gate = [0] * (g+1)
p = int(input())
answer = 0

arr = [int(input()) for _ in range(p)]

for gi in arr:
    count = gi
    while count :
        if not gate[count] :
            gate[count] = gi
            break
        count -= 1
    if count == 0 :
        break
    answer += 1
print(answer)
"""

import sys

input = sys.stdin.readline

g = int(input())
gate = [0] * (g+1)
p = int(input())
answer = 0

arr = [int(input()) for _ in range(p)]

parent = [i for i in range(g+1)]


def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):  # x > y
    root_x = find(x)
    root_y = find(y)
    parent[root_x] = root_y #root_y를 루트로

for gi in arr:
    now = find(gi)
    if now == 0:
        break
    union(now, now - 1)
    answer += 1
print(answer)