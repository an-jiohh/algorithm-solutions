
a = list(input())
b = list(input())

n = len(a)
m = len(b)

dp = [[0] * (m+1) for i in range(n+1)]
answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)
print(answer)

# 실패이유
# 메모리 초과
# python과 pypy는 가비지 콜렉터의 구현이 다름
# 메모리초과 발생시 pypy와 print이 효율적일 수도 있닥고함
# pypy로 제출하여 풀이
