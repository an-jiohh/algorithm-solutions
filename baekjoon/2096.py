import sys

input = sys.stdin.readline

n = int(input())

min_dp = [0,0,0]
max_dp = [0,0,0]

for _ in range(n) :
    a,b,c = map(int, input().split())
    left, mid, right = min_dp
    min_dp = [min(left, mid) + a, min(left, mid, right) + b ,min(mid, right) + c]
    left, mid, right = max_dp
    max_dp = [max(left, mid) + a, max(left, mid, right) + b ,max(mid, right) + c]
print(max(max_dp),min(min_dp))