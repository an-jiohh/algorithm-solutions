n = int(input())

prime_check = [False, False] + [True] * n
prime = []

for i in range(2, n+1):
    if prime_check[i] :
        for j in range(i * 2, n+1,i):
            prime_check[j] = False
        prime.append(i)

start, end = 0, 0
num = 0
answer = 0

while True :
    if num >= n :
        num -= prime[start]
        start += 1
    else :
        if end == len(prime) :
            break
        num += prime[end]
        end += 1
    if num == n :
        answer += 1
print(answer)