import sys

input = sys.stdin.readline

n = int(input())
arr = [[]for i in range(n)]

arr[0] = [0, int(input())]
for i in range(1,n) :
    now = int(input())
    arr[i].append(max(arr[i-1]))
    arr[i].append(arr[i-1][0]+now)
    arr[i].append(arr[i-1][1]+now)
print(max(arr[-1]))