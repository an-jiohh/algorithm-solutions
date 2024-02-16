n = int(input())
arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:[x[1],x[0]])
count, check = 0, 0
for i in arr :
    if check <= i[0] :
        check = i[1]
        count += 1
print(count)
