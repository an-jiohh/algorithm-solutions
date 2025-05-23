from itertools import combinations_with_replacement

def solution(n, s):
    answer = [-1]
    answer_check = 0
    arr = []
    for i in range(1, s):
        arr.append(i)
    arr = list(combinations_with_replacement(arr, n))
    for i in arr :
        a,b = 0, 1
        for j in i :
            a += j
            b *= j
        if a == s and answer_check <= b :
            answer_check, answer = b, i
    return list(answer)

#---

#dfs -> n개 이상 더해지거나, s보다 커질경우 백트래킹
import sys
sys.setrecursionlimit(10000)  # 최대 재귀 깊이를 10,000으로 설정

answer_list = []
from itertools import combinations_with_replacement

def solution(n, s):
    # arr = [i for i in range(1,s)]
    # 굳이 만들 필요가 없음
    
    def dfs(start, sum_num, num_list) :
        global answer_list
        if len(num_list) == n:
            if sum_num == s :
                answer_list.append(num_list[:])
            return
        if sum_num >= s :
            return
        for i in range(start, s) :
            if sum_num + i > s :
                break
            num_list.append(i)
            dfs(i, sum_num + i, num_list)
            num_list.pop()
    
    dfs(1, 0, [])
    if not answer_list :
        return [-1]
    answer,answer_sum = [], 0
    for i in answer_list :
        result = 1
        for j in i :
            result *= j
        if result > answer_sum :
            answer = i
        
    return answer

#---
# 최종풀이

def solution(n, s):
    q,r = s // n, s % n
    if q == 0 : return [-1]
    answer = [q] * n
    for i in range(r) : answer[i] += 1
    answer.sort()
    return answer