#

import sys

input = sys.stdin.readline

T = int(input())

dp = [0,1,1,1,2,2,3,4,5,7,9]

for t in range(T):
    n = int(input())
    for i in range(len(dp),n+1):
        dp.append(dp[i-2]+dp[i-3])    
    print(dp[n])