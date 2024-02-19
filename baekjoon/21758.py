import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

first_bee = sum(arr) - arr[0]
second_bee = first_bee
cnt = sum(arr)-arr[0]-arr[-1]+max(arr[1:-1])

for i in range(1, n-1) :
    honey = arr[i]
    first_bee -= honey
    second_bee -= honey
    cnt = max(cnt, first_bee + second_bee)
    first_bee += honey

first_bee = sum(arr) - arr[-1]
second_bee = first_bee
for i in range(n-2, 0, -1) :
    honey = arr[i]
    first_bee -= honey
    second_bee -= honey
    cnt = max(cnt, first_bee + second_bee)
    first_bee += honey

print(cnt)