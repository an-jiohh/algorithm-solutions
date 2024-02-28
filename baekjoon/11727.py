n = int(input())

arr = [0] * (n + 1)
arr[0] = 1
arr[1] = 3
for i in range(2,n):
    arr[i] = arr[i-1] + arr[i-2] * 2
print(arr[n-1] % 10007)