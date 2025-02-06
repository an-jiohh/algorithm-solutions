from collections import deque

n, k = map(int, input().split())

answer = []
queue = deque([i for i in range(1,n+1)])

count = 1

while queue :
    if count == k :
        answer.append(queue.popleft())
        count = 1
    else :
        queue.append(queue.popleft())
        count += 1

print("<", end="")
for i in answer[:-1] :
    print(i, end=", ")
print(answer[-1], end="")
print(">", end="")