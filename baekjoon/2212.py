n = int(input())
k = int(input())

arr = list(map(int, input().split()))
arr.sort()
arr_index = [arr[i]-arr[i-1] for i in range(1,n)]
arr_index.sort()

print(sum(arr_index[:n-k]))