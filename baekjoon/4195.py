# 친구 관계가 생긴 순서대로 주어졌을때, 두 사람의 친구 네트워크에 몇명이 있는지 구하는 프로그램을 만드는 문제
# 친구 네트워크란 친구 관계 만으로 이동할 수 있는 사이

import sys

input = sys.stdin.readline

f = int(input())

parent = {}
rank = {}

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y :
        return size[root_x]
    if rank[root_x] < rank[root_y] :
        parent[root_x] = root_y
        size[root_y] += size[root_x]
        return size[root_y]
    else :
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        if rank[root_x] == rank[root_y] :
            rank[root_x] += 1
        return size[root_x]

def init(x):
    if x not in parent :
        parent[x] = x
        rank[x] = 1
        size[x] = 1

for _ in range(f):
    parent = {}
    rank = {}
    size = {}
    n = int(input())
    for j in range(n):
        a, b = input().split()
        init(a)
        init(b)
        result = union(a, b)
        print(result)