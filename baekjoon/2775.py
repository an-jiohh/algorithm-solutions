import sys

input = sys.stdin.readline

t = int(input())

arr = [[i for i in range(1, 15)]]

for i in range(t):
    k = int(input())
    n = int(input())
    while len(arr) <= k :
        temp, count = [], 0
        for j in arr[-1] :
            count += j
            temp.append(count)
        arr.append(temp)
    print(arr[k][n-1])