n = int(input())

arr = list(map(int, input().split()))

lis = arr[:]

for i in range(n) :
    for j in range(i) :
        if arr[i] > arr[j] :
            lis[i] = max(lis[i], arr[i]+lis[j])
        
print(max(lis))