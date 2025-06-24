import sys
sys.setrecursionlimit(10**9)

n = int(input())

arr = [input() for i in range(n)]
def quard(x,y,n):
    for i in range(x,x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j] : #모든 조건이 같지않으니 분할해야함, 
                # 분할할때 그 노드부터하는게 아니라 전체를 분할
                half_n = n // 2
                result = "("
                result += quard(x,y,half_n)
                result += quard(x,y+half_n, half_n)
                result += quard(x+half_n, y, half_n)
                result += quard(x+half_n, y+half_n, half_n)
                result += ")"
                return result
    return arr[x][y]


print(quard(0,0,n))