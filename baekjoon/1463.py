from collections import deque

x = int(input())
arr = {}
queue = deque([[x,1]])
count = 0
while queue :
    t,count = queue.popleft()
    if t < 1 : continue
    if t == 1 : break
    if t not in arr :
        arr[t] = 1 
        if t % 3 == 0 :
            queue.append([t // 3, count+1])
        if t % 2 == 0 :
            queue.append([t // 2, count+1])
        queue.append([t - 1, count+1])

print(count-1)