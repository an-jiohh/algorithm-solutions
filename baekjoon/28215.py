from itertools import combinations

n, k = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(n)]
node = [i for i in range(n)]

com_node = combinations(node, k)
answer = 10000000
for i in com_node:
    temp_nodes = []
    for j in node :
        m = 10000000
        y2, x2 = arr[j]
        for k in i :
            y1, x1 = arr[k] 
            temp = abs(x1-x2) + abs(y1-y2)
            m = min(m, temp)
        temp_nodes.append(m)
    max_node = max(temp_nodes)
    answer = min(answer, max_node)

print(answer)