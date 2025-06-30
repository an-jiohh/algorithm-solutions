import sys

input = sys.stdin.readline

while True :
    m,n = map(int, input().split())

    if m == 0 and m == 0 : break

    parent = [i for i in range(m+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y :
            parent[root_y] = root_x

    graph = []
    answer,counter = 0, 0
    for i in range(n) :
        temp = list(map(int,input().split()))
        graph.append(temp)
        answer += temp[2]

    graph.sort(key= lambda x:x[2])
    
    for a,b,c in graph :
        if find(a) != find(b):
            union(a,b)
            counter += 1
            answer -= c
            if counter == m-1:
                break
    print(answer)