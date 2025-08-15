# 챕터당 완성시 이전것이랑 합침
# 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합
# 한 개의 파일을 완성하는데 필요한 비용의 총 합
# 두 개의 파일을 하나로 합치고 이 임시파일을 또 다른 파일과 합쳐야함
# python시간 초과로 java로 풀이

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    pre_sum = [0] * (n + 1)
    for i in range(1,n+1):
        pre_sum[i] = pre_sum[i-1]+arr[i-1]
    dp = [[0] * n for i in range(n)]

    def dfs(start, end):
        if start == end :
            return 0
        
        if dp[start][end] != 0:
            return dp[start][end]
        
        temp = 10**9
        for i in range(start, end):
            temp = min(temp, dfs(start, i) + dfs(i+1, end)+ pre_sum[end + 1]-pre_sum[start])
        dp[start][end] = temp
        return temp
    print(dfs(0,n-1))