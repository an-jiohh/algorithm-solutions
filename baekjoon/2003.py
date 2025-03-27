n, m = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
count = arr[start]
answer = 0

while start < n and end < n :
    if count == m :
        answer += 1
    if count <= m and end < n - 1 :
        end += 1
        count += arr[end]
    else :
        if start < n :
            count -= arr[start]
        start += 1
print(answer)
