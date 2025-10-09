# 이친수
# 0으로 시작하지 않는다
# 1이 두번연속으로 나타나지 않는다.
# n이 주어졌을 때, N자리 이천수의 개술르 구하는 프로그램

"""
N = int(input())
answer = 0
def dfs(post, n):
    global answer
    if n == N :
        answer += 1
        return
    if post == 0 : dfs(1, n+1)
    dfs(0, n+1)

dfs(1,1)

print(answer)
"""
n = int(input())

if n == 1: print(1)
else :
    a,b = 1,0 # a = 1, b = 0
    for i in range(1,n):
        a,b = b, a+b
    print(a+b)