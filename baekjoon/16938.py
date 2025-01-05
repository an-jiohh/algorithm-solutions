n, l, r, x = map(int, input().split())

arr = list(map(int, input().split()))

from itertools import combinations

count = 0 
for i in range(2,len(arr)+1) :
    com = list(combinations(arr, i))
    for j in com :
        min_num, max_num = min(j), max(j)
        temp = sum(j)
        if l <= temp <= r and max_num-min_num >= x :
            count += 1

print(count)