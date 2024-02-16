n, won = map(int, input().split())

arr = []
answer = 0
for i in range(n):
    arr.append(int(input()))
arr.sort()
while won :
    coin = arr.pop()
    answer += (won // coin)
    won = won % coin

print(answer)