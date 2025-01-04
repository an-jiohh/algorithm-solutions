n, l, r, x = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = 1
sum = arr[start] + arr[end]

while len(arr) == start :
    if sum 