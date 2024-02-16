n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = (10**10, 10**10)

def binary_search(n) :
    target = -arr[n]
    a, b = n+1, len(arr) - 1
    while a < b :
        mid = (a+b) // 2
        if arr[mid] < target : a = mid + 1
        else : b = mid
    return a

for i in range(n-1) :
    temp = binary_search(i)
    if i < temp and abs(sum(m)) > abs(arr[i]+arr[temp]) :
        m = (arr[i], arr[temp])
    if i < temp - 1 and abs(sum(m)) > abs(arr[i]+arr[temp-1]) :
        m = (arr[i], arr[temp-1])

for i in m:
    print(i, end=" ")

'''
## bisect를 이용한 풀이
from bisect import bisect_left, bisect_right

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = (10**10, 10**10)

def binary_search(n) :
    target = -arr[n]
    a, b = n+1, len(arr) - 1
    while a < b :
        mid = (a+b) // 2
        if arr[mid] < target : a = mid + 1
        else : b = mid
    return a

for i in range(n-1) :
    temp = bisect_right(arr, -arr[i])
    if i < temp and abs(sum(m)) > abs(arr[i]+arr[temp]) :
        m = (arr[i], arr[temp])
    if i < temp - 1 and abs(sum(m)) > abs(arr[i]+arr[temp-1]) :
        m = (arr[i], arr[temp-1])

for i in m:
    print(i, end=" ")
'''