n,m,k = map(int, input().split())

A = list(map(int, input().split()))
a_sort = []
for i in range(n):
    a_sort.append((A[i],i+1))
a_sort.sort()

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

for i in range(m):
    a,b = map(int, input().split())
    union(a,b)
answer = 0
for i in range(0,n):
    score,target = a_sort[i]
    if find(0) != find(target):
        answer += score
        union(0,target)

if answer > k :
    print("Oh no")
else :
    print(answer)