# n*n 도시, 1칸로 나누어져있음, 
# 각칸은 빈칸 0, 치킨집 2, 집 1
# r = 행, c = 열, 위에서부터 1
# 치킨거리 = 집과 가장 치킨집사이의 거리  = |r1-r2| + |c1-c2|
# 치킨집의 폐업 시킬려할때, 치킨집의 최대개수는 M개
# 이때 도시의 치킨거리가 가장 작게될값을 구하는 문제

# 치킨거리를 꼭구해야함으로 도시의 치킨거리를 전체를 구해야함 

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

chi = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chi.append((i,j))

count = [[n*n] * len(home) for _ in range(len(chi))]
for i in range(len(home)) :
    home_y, home_x = home[i]
    for j in range(len(chi)) :
        chi_y, chi_x = chi[j]
        count[j][i] = min(abs(home_y-chi_y) + abs(home_x-chi_x), count[j][i])

answer = 0

if len(count) > m:
    count.sort(key=lambda x:sum(x))
    for i in range(len(count)-m):
        count.pop()

for i in range(len(home)):
    temp = n*n
    for j in range(len(count)):
        temp = min(count[j][i], temp)
    answer += temp

print(answer)

# 7 2
# 0 2 0 0 0 0 0
# 2 1 2 0 0 0 0
# 0 2 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 2 0 1
"""
from itertools import combinations

import sys

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

chi = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chi.append((i,j))
combi = combinations(chi, m)


answer = n**n
for chi in combi :
    count = 0
    for home_y, home_x in home :
        temp = n*n
        for chi_y, chi_x in chi :
            temp = min(abs(home_y-chi_y) + abs(home_x-chi_x), temp)
        count += temp
    answer = min(answer, count)


print(answer)
