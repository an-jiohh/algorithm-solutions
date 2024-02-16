from collections import deque

n, k = map(int, input().split())

queue = deque([(n,0)])
visited = {n:1}
count = 0

def insert_node(node,count):
    queue.append((node,count+1))
    visited[node] = 1

while queue :
    node,count = queue.popleft()
    if node == k : break
    if node * 2 not in visited and node * 2 <= 100000: insert_node(node*2,count)
    if node + 1 not in visited and node + 1 <= 100000: insert_node(node+1,count)
    if node - 1 not in visited and node - 1 >= 0: insert_node(node-1,count)

print(count)