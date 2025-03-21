#가짓수를 가장 많이 먹는 조건
# 1. 벨트위에 가장 많이 먹는 조건 찾기, 이때 쿠폰이 포함되지 않게
# 2. 쿠폰으로 현재 밸트위에 없는 음식을 먹고
import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
counter = [0] * (d + 1)
counter[c] = 1
count = 1
sw = deque()
answer = 0

for i in arr[-k:] :
    if counter[i] == 0 :
        count += 1
    counter[i] += 1
    sw.append(i)


for i in arr :
    temp = sw.popleft()
    counter[temp] -= 1
    if counter[temp] == 0 :
        count -= 1

    if counter[i] == 0:
        count += 1
    counter[i] += 1
    sw.append(i)
    answer = max(count, answer)
print(answer)