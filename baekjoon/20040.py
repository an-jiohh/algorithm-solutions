# 두명의 플레이어가 차례로 게임
#  선 플레이어가 홀수 번째 차례를, 후 플레이어가 짝수 번째 차례
# 게임 시작 시 0 부터 n − 1 까지 고유한 번호가 부여된 평면 상의 점 n 개
# 두 점을 선택해서 이를 연결하는 선분을 긋는데, 이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차하는 것은 가능
# 처음으로 사이클을 완성하는 순간 게임이 종료
# 게임의 진행 상황이 주어지면 몇 번째 차례에서 사이클이 완성되었는지, 또는 진행중인지 판단

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

parent = [i for i in range(n)]
rank = [1 for i in range(n)]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x == parent_y :
        return True
    # parent[parent_x] = parent_y 최적화 전
    if rank[parent_x] > rank[parent_y] :
        parent[parent_y] = parent_x
    else :
        parent[parent_x] = parent_y
        if rank[parent_x] == rank[parent_y] :
            parent_y += 1
    
answer = 1
for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        break
    answer += 1

if answer == m + 1 :
    answer = 0
print(answer)