from collections import deque

n = int(input())

arr = list(map(int, input().split()))

sum_arr = [0]

for i in arr :
    sum_arr.append(sum_arr[-1] + i)

queue = deque()

for i in range(1, n-2):
    queue.append((i, sum_arr[i], 3))

answer = 0
if sum_arr[n] % 4 == 0 :
    while queue :
        start, check, count = queue.popleft()
        if count == 1 :
            if sum_arr[n] - sum_arr[start] == check :
                answer += 1
            continue
        for i in range(start + 1, n - count + 2) : # 2 2
            if sum_arr[i] - sum_arr[start] == check :
                queue.append((i, check, count-1))

print(answer)