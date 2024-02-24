import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1,n+1) :
    arr[i] = arr[i-1] + arr[i]

for i in range(m) :
    start, end = map(int, input().split())
    print(arr[end]-arr[start-1])