n, k = map(int, input().split())

arr = list(input())

answer = 0

for i in range(n):
    if arr[i] == 'H' :
        for j in range(i-k, i+k+1):
            if 0 <= j < n and arr[j] == "P" and  abs(j-i) <= k :
                arr[j] = 0
                answer += 1
                break
print(answer)