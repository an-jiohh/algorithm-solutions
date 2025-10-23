"""
# 실수할 경우도 포함하는 풀이법으로 일부테스트에서 실패
answer = [[],[]]
def solution(board, aloc, bloc):
    ny = len(board)
    nx = len(board[0])
    def dfs(ay,ax,by,bx,count, position):
        global answer
        if board[ay][ax] == 0 :
            answer[position].append(count)
            return
        check = False
        for my, mx in [(0,1),(0,-1),(1,0),(-1,0)]:
            my, mx = ay + my, ax + mx
            if 0 <= my < ny and 0 <= mx < nx and board[my][mx] == 1:
                check = True
                board[ay][ax] = 0
                dfs(by,bx,my,mx,count+1,not position)
                board[ay][ax] = 1
        if check == False :
            answer[position].append(count)
            return
    dfs(aloc[0],aloc[1],bloc[0],bloc[1],0,1)
    if answer[0] :
        return max(answer[0])
    else :
        return min(answer[1])
    return answer
"""
#핵심 이길 수 있으면 최소 턴 승, 지면 최대 패로 구함

def solution(board, aloc, bloc):
    n = len(board)
    m = len(board[0])
    answer = -1
    def dfs(ay,ax,by,bx):
        check = False
        if board[ay][ax] == 0 :
            return (False, 0)
        
        win_turns = []
        lose_turns = []
        for my,mx in [(0,1),(0,-1),(1,0),(-1,0)]:
            my, mx = my+ay, mx+ax
            win, turns = 0,0
            if 0 <= my < n and 0 <= mx < m and board[my][mx] :
                check = True
                board[ay][ax] = 0
                win,turns = dfs(by,bx,my,mx)
                board[ay][ax] = 1
                if win : # 결과를 뒤집어서 입력
                    lose_turns.append(turns+1)
                else :
                    win_turns.append(turns+1)
        if not check :
            return (False, 0) # 이번턴은 패배
        if win_turns :
            return (True, min(win_turns))
        else :
            return (False, max(lose_turns))
    _, answer = dfs(aloc[0],aloc[1],bloc[0],bloc[1])
    return answer