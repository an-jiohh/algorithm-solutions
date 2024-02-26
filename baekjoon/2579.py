import sys

input = sys.stdin.readline

n = int(input())

stairs = [0] * 300 # n이 아닌 300을 곱해주는 이유 : 아래에서 indexError가 발생하기 때문
dp = [0] * 300

for i in range(n) :
    stairs[i] = int(input()) #append를 사용하지 않는 이유 밑에 초기화 때문에 indexError가 발생한다.

dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3,n) :
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[n-1])