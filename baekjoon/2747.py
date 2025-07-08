n = int(input())

arr = [0, 1, 1, 2]

while len(arr) <= n :
    arr.append(arr[-1]+arr[-2])
print(arr[n])