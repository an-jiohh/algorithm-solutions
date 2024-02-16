import sys

input = sys.stdin.readline

n = int(input())

dp = [0,0,int(input()),0]

for i in range(n-2):
    temp = int(input())
    print(dp)
    dp[0], dp[1],dp[2] = max(dp), dp[0] + temp, dp[1] + temp

print(dp)
print(max(dp[:-1])+int(input()))