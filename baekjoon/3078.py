import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [input().strip() for _ in range(n)]

queue = deque()
check = [0] * 21
answer = 0
for i in range(n):
    node = len(arr[i])
    if i > k :
        temp = queue.popleft()
        check[temp] -= 1
    if check[node] :
        answer += check[node]
    check[node] += 1
    queue.append(node)

print(answer)