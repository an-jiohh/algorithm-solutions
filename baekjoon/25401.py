n = int(input())

arr = list(map(int, input().split()))
answer = 501
for i in range(n):
    for j in range(i+1, n):
        diff = (arr[j] - arr[i]) // (j - i)

        if diff - int(diff) != 0 :
            continue

        count = 0
        start = arr[i] - diff * i
        diff  = int(diff)
        for k in range(n) :
            if arr[k] != start:
                count+=1
            start += diff
        answer = min(answer, count)
print(answer)

"""
중간에 다른 풀이로 변경
n = int(input())

arr = list(map(int, input().split()))
answer = 501
for i in range(len(arr)):
    mid = arr[i]
    desc, asc, same = 0, 0, 0
    desc_temp, asc_temp = mid, mid
    for j in range(i-1,-1,-1):
        desc_temp, asc_temp = (desc_temp+1), (asc_temp-1)
        if desc_temp != arr[j] :
            desc += 1
        if asc_temp != arr[j] :
            asc += 1
        if mid != arr[j] : same += 1
    desc_temp, asc_temp = mid, mid
    print(answer, desc, asc, same, end="//")
    for j in range(i+1,len(arr)):
        desc_temp, asc_temp = (desc_temp-1), (asc_temp+1)
        if desc_temp != arr[j] :
            desc += 1
        if asc_temp != arr[j] :
            asc += 1
        if mid != arr[j] : same += 1
    print(answer, desc, asc, same)
    answer = min(answer, desc, asc, same)
print(answer)
"""