import sys

input = sys.stdin.readline

arr = list(input().strip())
s_arr = set(arr)
d_arr = dict()

for i in s_arr :
    d_arr[i] = [0]

for i in arr :
    for j in s_arr:
        d_arr[j].append(d_arr[j][-1])
    d_arr[i][-1] += 1 

q = int(input())

for i in range(q):
    a, l, r = input().split()
    if a in d_arr:
        print(d_arr[a][int(r) + 1] - d_arr[a][int(l)])
    else:
        print(0)