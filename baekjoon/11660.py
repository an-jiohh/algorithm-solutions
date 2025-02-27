import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    temp = [0] + list(map(int, input().split()))
    for j in range(1, n+1) :
        temp[j] = temp[j] + temp[j-1]
    arr.append(temp)
        
for i in range(m):
    answer = 0
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(y1-1, y2):
            answer += arr[j][x2] - arr[j][x1-1]
    print(answer)