import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


parent = []
rank = []
is_cycle = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y :
        is_cycle[root_x] = True
    if rank[root_x] < rank[root_y] :
        parent[root_x] = root_y
        if is_cycle[root_x] and is_cycle[root_y] :
            is_cycle
    else :
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
case = 1
while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    parent = [i for i in range(n+1)]
    rank = [1] * (n+1)
    is_cycle = [False] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        union(a, b)

    tree_count = 0
    for i in range(1, n+1):
        if find(i) == i and not is_cycle[i]:
            tree_count += 1
    print(f"Case {case}: ", end="")
    if tree_count == 0:
        print("No trees.")
    elif tree_count == 1:
        print("There is one tree.")
    else :
        print(f"A forest of {tree_count} trees.")
    case += 1
