n = int(input())

arr = list(map(int, input().split()))
lis = [1 for i in range(n)]
for i in range(n) :
    for j in range(i) :
        if arr[i] > arr[j] :
            lis[i] = max(lis[i], lis[j] + 1)

lisr = [1 for i in range(n)]
for i in range(n-1,-1,-1) :
    for j in range(n-1,i-1,-1) :
        if arr[i] > arr[j] and lisr[i] <= lisr[j] :
            lisr[i] = lisr[j] + 1

answer = 0
for i in range(n) :
    answer = max(answer, lis[i]+lisr[i]-1)

print(answer)