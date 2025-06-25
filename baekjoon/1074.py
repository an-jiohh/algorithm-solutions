import sys
sys.setrecursionlimit(10**9)

N, r, c = map(int, input().split())
answer = 0
def quard(y,x,n):
    global answer
    if y == r and x == c :
        print(answer)
        return

    if not (y<= r < y+n and x <= c < x+n) :
        answer += n*n
        return
    
    n = n // 2
    quard(y, x, n)
    quard(y, x+n,n)
    quard(y+n, x, n)
    quard(y+n, x+n,n)

quard(0,0,2**N)