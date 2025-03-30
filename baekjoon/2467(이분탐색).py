n = int(input())

arr = list(map(int, input().split()))
m = (10**10,0)
for i in range(n-1):
    now = -arr[i]
    a, b = i+1, n - 1
    while a < b :
        mid = (a + b) // 2
        if now > arr[mid] : a = mid + 1
        else : b = mid
    if i < a and abs(arr[a] + arr[i]) < abs(m[0] + m[1]) :
        m = (arr[i], arr[a])
    if i < a - 1 and abs(arr[a-1] + arr[i]) < abs(m[0] + m[1]) :
        m = (arr[i], arr[a-1])

print(*m)