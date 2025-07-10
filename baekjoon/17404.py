# n개의 집, 거리는 선분으로
# 빨강, 초록, 파랑 중 하나의 색으로 칠함, 모든 집을 칠하는 비용의 최솟값
# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

import sys

input = sys.stdin.readline

n = int(input())

rgb = [list(map(int, input().split())) for i in range(n)]
answer = []

def find(start):
    arr = [10**9,10**9,10**9] #r,g,v
    arr[start] = rgb[0][start]
    for r,g,b in rgb[1:] :
        pre_r, pre_g, pre_b = arr
        arr[0] = min(pre_g + r, pre_b + r)
        arr[1] = min(pre_r + g, pre_b + g)
        arr[2] = min(pre_r + b, pre_g + b)
    arr.pop(start)
    return min(arr)
answer.append(find(0))
answer.append(find(1))
answer.append(find(2))
print(min(answer))