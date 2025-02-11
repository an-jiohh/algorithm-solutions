from collections import deque

n, d, k, c = map(int, input().split())

arr = [int(input())for _ in range(n)]

de_arr = deque(arr)

m = 0
for _ in range(n):
    temp = set()
    for i in range(k):
        temp.add(de_arr[i])
    temp.add(c)
    m = max(m, len(temp))
    de_arr.append(de_arr.popleft())

print(m)