n, k  = map(int, input().split())

arr = list(map(int, input().split()))
arr_index = [arr[i]-arr[i-1] for i in range(1, n)]
arr_index.sort()
print(sum(arr_index[:n-k]))