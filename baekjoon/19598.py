import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = [tuple(map(int, input().split())) for i in range(n)]
room = []

arr.sort()

for i in arr :
    start, end = i
    if room and room[0] <= start :
        heapq.heappushpop(room, end)
    else : heapq.heappush(room, end)

print(len(room))