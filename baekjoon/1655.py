import heapq
import sys

input = sys.stdin.readline

n = int(input())

center = int(input())
print(center)
left_queue = []
right_queue = []


for i in range(1,n):
    num = int(input())
    if center < num :
        heapq.heappush(right_queue, num)
    else :
        heapq.heappush(left_queue, -num)
    if len(left_queue) > len(right_queue) :
        heapq.heappush(right_queue, center)
        center = -heapq.heappop(left_queue)
    elif len(left_queue) + 1 < len(right_queue):
        heapq.heappush(left_queue, -center)
        center = heapq.heappop(right_queue)
    print(center)