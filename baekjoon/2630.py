# 파란색 + 흰색이 섞여있는 종이에서
# 각 색만있는 종이로 계속해서 1/4로 자를때 흰색종이와 파란색 종이의 갯수를 구하는 문제

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
answer = [0, 0] # 하얀색, 파란색

def quard(y,x,n):
    check = arr[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j] != check :
                n = n // 2
                quard(y,x,n)
                quard(y,x+n,n)
                quard(y+n,x,n)
                quard(y+n,x+n,n)
                return
    answer[check] += 1
quard(0,0,n)
print(answer[0])
print(answer[1])