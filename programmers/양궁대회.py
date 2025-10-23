answer_score = 0
answer = []

def solution(n, info):
    info_count = sum(info)
    arrows = [0] * 11
    def dfs(i,r_score, a_score, arrow, arrow_count):
        global answer_score, answer
        if i == 11:
            if arrow_count == 0 and answer_score < r_score - a_score :
                answer_score = r_score - a_score
                answer = [arrow[:]]
            elif arrow_count == 0 and answer_score == r_score - a_score :
                answer.append(arrow[:])
            return 
        for j in range(0,arrow_count+1):
            arrow[i] = j 
            if j == info[i] == 0 :
                dfs(i+1,r_score, a_score, arrow, arrow_count)
            elif j <= info[i] :
                dfs(i+1,r_score, a_score + 10 - i, arrow, arrow_count - j)
            else :
                dfs(i+1,r_score + 10 - i, a_score, arrow, arrow_count - j)
            arrow[i] = 0
    dfs(0,0,0,arrows,n)
    if answer_score <= 0 : 
        return [-1]
    answer.sort(key=lambda x:x[::-1], reverse=True)
    return answer[0]