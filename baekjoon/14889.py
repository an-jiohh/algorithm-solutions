# n명의 사람
# 1~n범위 내에있는 ij를 바탕으로 이차원 배열 s에 능력치
# sij, sji는 같은팀이 되었을때 시너지가 되는 추가 능력치
# 이떄 팀 추가 능력치가 동등한 경우를 능력치 차를 찾는 문제
# n = 20, 20 * 20 = 400

#시너지 처리 방법 = 각각 이미들어간 원소들도 비교해가면서 시너지를 비교해야할 수도
#1. 전체 조합의 수를 구한 후 시너지 비교
#2. 원소를 구하면서 시너지를 더한 후 비교

from itertools import combinations

n = int(input())

arr = []
max_score = 0

for i in range(n):
    temp = list(map(int,input().split()))
    max_score += sum(temp)
    arr.append(temp)

temp_combination = list(combinations(range(n), n//2))
answer = max_score
for node in temp_combination :
    nodes = set(map(int, node))
    link_count = 0
    start_count = 0
    for i in range(n):
        for j in range(n):
            if i in nodes and j in nodes :
                link_count += arr[i][j]
            elif i not in nodes and j not in nodes : start_count += arr[i][j]
    answer = min(answer, abs(link_count - start_count))
print(answer)