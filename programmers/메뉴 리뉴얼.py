# 가장 많이 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 2가지 이상의 단품메류로, 2명이상의 손님으로부터 주문된 단품메뉴를 포함
from itertools import combinations

def solution(orders, course):
    answer = []
    d = {}
    for order in orders:
        for i in course:
            result = combinations(order, i)
            for j in result:
                j = list(j)
                j.sort()
                j = tuple(j)
                d[j] = d.get(j, 0) + 1
    for i in course :
        count, temp = 2, []
        for j in d :
            if len(j) == i :
                if d[j] > count :
                    count = d[j]
                    temp = ["".join(j)]
                elif d[j] == count :
                    temp.append("".join(j))
        answer += temp
    answer.sort()
    return answer