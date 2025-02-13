n = int(input())

arr = [i for i in range(1, n+1)]

while len(arr) != 1 :
    temp = []
    for i in range(0, len(arr)):
        if (i + 1) % 2 == 0 :
            temp.append(arr[i])
    arr = temp
print(*arr) 