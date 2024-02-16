import sys

input = sys.stdin.readline

n = int(input())
arr = [0,0,0]

for i in range(n) :
    r,g,b = map(int, input().split())
    pre_r, pre_g, pre_b = arr
    r = min(pre_g+r,pre_b+r)
    g = min(pre_r+g, pre_b+g)
    b = min(pre_r+b, pre_g+b)
    arr = [r,g,b]

print(min(arr))