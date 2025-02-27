n = int(input())

answer = []
answer.append(n // 300)
n = n % 300
answer.append(n // 60)
n = n % 60
answer.append(n // 10)
n = n % 10

if n == 0 :
    print(*answer)
else : print(-1)