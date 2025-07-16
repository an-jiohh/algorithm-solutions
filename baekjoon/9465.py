import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int ,input().split()))
    b = list(map(int, input().split()))
    check = [0,a[0],b[0]]
    for i in range(1,n):
        check_a = max(check[0], check[2]) + a[i]
        check_b = max(check[0], check[1]) + b[i]
        check_0 = max(check)
        check = [check_0, check_a, check_b]
    print(max(check))