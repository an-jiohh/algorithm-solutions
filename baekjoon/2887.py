    # n = 100,000으로 n**2으로 풀이시 시간초과발생
    # nlogn으로 풀어야하는데...
    # 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)으로 
    # x의 거리차이, y의 거리차이, z의 거리차이 중 작은 것
    # ?(x,y,x)를 기준으로 정렬할 경우 ?에

import sys

input = sys.stdin.readline

n = int(input())

node = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    node[i].append(i)
x_node = sorted(node, key= lambda x:x[0])
y_node = sorted(node, key= lambda x:x[1])
z_node = sorted(node, key= lambda x:x[2])

graph = []

def distanse(a,b,xyz):
    axyz = a[xyz]
    bxyz = b[xyz]
    return abs(axyz - bxyz)
                 
def create_list(nodes, xyz):
    a = 0
    for b in range(1,n):
        cost = distanse(nodes[a],nodes[b],xyz)
        graph.append((nodes[a][3],nodes[b][3],cost))
        a = b

create_list(x_node,0)
create_list(y_node,1)
create_list(z_node,2)

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_x] = root_y
graph.sort(key = lambda x:x[2])
answer, count = 0, 0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a,b)
        answer += c
        count += 1
        if count == n-1:
            break

print(answer)