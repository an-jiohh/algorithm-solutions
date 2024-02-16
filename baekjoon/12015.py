from bisect import bisect_left, bisect_right

n = int(input())

arr = list(map(int, input().split()))

lis = [1 for i in range(n)]
dp = [0]

for i in range(n) :
    temp = bisect_left(dp, arr[i])
    if temp == len(dp) : dp.append(arr[i])
    elif dp[temp] > arr[i] : dp[temp] = arr[i]
    lis[i] = temp
print(lis)
print(max(lis))