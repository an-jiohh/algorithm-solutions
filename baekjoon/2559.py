n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr_sum = [0]
total = 0
for i in arr:
    total += i
    arr_sum.append(total)

answer = arr_sum[k]
for i in range(k,n+1):
    temp = arr_sum[i] - arr_sum[i-k]
    answer = max(answer, temp)
print(answer)