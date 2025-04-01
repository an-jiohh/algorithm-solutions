n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
while start <= end :
    mid = (start + end) // 2

    temp, count = 0, 1
    for i in arr :
        if temp + i <= mid :
            temp += i
        else :
            count += 1
            temp = i
    if count > m :
        start = mid + 1
    else :
        end = mid - 1
print(start)