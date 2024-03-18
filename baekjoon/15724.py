import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(m+1)]

for i in range(1,n+1) :
    arr.append([0] + list(map(int, input().split())))
    for j in range(1, m+1):
        arr[i][j] = arr[i][j] + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] 

k = int(input())

for i in range(k):
    cnt = 0
    y1,x1,y2,x2 = map(int, input().split())
    print(arr[y2][x2]-arr[y2][x1-1]-arr[y1-1][x2]+arr[y1-1][x1-1])