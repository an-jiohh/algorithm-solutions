n, k = map(int, input().split())

for i in range(1,k+1):
    n -= i

answer = k - 1
if n < 0 :
    answer = -1
elif n % k != 0 :
    answer += 1
print(answer)