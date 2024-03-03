import sys

input = sys.stdin.readline

n = int(input())

answer = [int(input())]

for i in range(n-1):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if i == 0 :
            arr[i] += answer[0]
        elif i == len(arr) - 1 : 
            arr[i] += answer[-1]
        else :
            temp = max(answer[i],answer[i-1])
            arr[i] += temp
    answer = arr
print(max(answer))