# n+1개의 집합 0 ~ n이 있을때
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행
# 집합을 표현하는 프로그램

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

root = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y :
        return
    if rank[root_x] < rank[root_y] :
        root[root_x] = root_y
    else :
        root[root_y] = root_x
        if rank[root_x] == rank[root_y] :
            rank[root_x] += 1

for i in range(m):
    a,b,c = map(int, input().split())
    if a == 0 :
        union(b, c)
    else :
        if find(b) == find(c) : print("YES")
        else : print("NO")
