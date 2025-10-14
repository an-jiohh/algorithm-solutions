from itertools import permutations

# 원형을 두배하여 직선으로 변경
# 찾을때 시작점을 기준으로 전체길이만큼만 확인하면 쉽게 가능

# 시계방향만 탐색해도 확인가능
# weak = [1, 3, 11]
# dist = [2] 일 경우
# “1에서 반시계로 2칸 덮는다” = “11에서 시계로 2칸 덮는다”.가 성립하여 시계 방향만 탐색해도 가능하다
# 중요) 시작점이 고정돼 있는 문제의 경우에는 불가능

def solution(n, weak, dist):
    answer = 10 ** 9
    w = len(weak)
    weak = weak + [n + i for i in weak]
    for start in range(w) :
        target = weak[start:start+w]
        for orders in permutations(dist):
            check = True
            count = 1
            cover = target[0] + orders[0]
            for i in target:
                if cover < i :
                    count += 1
                    if count > len(orders) or count >= answer:
                        check = False
                        break
                    cover = i + orders[count-1]
            if check :
                answer = min(answer, count)
    if answer == 10 ** 9 : answer = -1
    return answer