import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n) :
    num = int(input())
    if num == 0 :
        temp = 0
        if heap : temp = heapq.heappop(heap)
        print(temp)
    else :
        heapq.heappush(heap, num)