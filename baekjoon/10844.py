n = int(input())

arr = [[1]*10 ]
arr[0][0] = 0
mod = 1000000000
for i in range(1, n):
    temp = []
    temp.append(arr[-1][1])
    for j in range(1,9):
        temp.append(arr[-1][j-1] + arr[-1][j+1] % mod)
    temp.append(arr[-1][8])
    arr.append(temp)
print(sum(arr[-1]) % mod)