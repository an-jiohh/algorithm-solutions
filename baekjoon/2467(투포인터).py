n = int(input())

arr = list(map(int, input().split()))

start, end = 0, n - 1
answer = (10 ** 9, 10 ** 9)

while start < end :
    if abs(answer[0] + answer[1]) >= abs(arr[start]  + arr[end]) :
        answer = (arr[start], arr[end])
    if arr[start] + arr[end] > 0 :
        end -= 1
    else :
        start += 1
print(*answer)