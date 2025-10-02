# 적은 건물을 공격하여 파괴
# 공격을 받으면 내구도 감소, 0이하가 되면 파괴
# 아군은 회복스킬을 사용하여 내구도를 높힘
# 공격을 받으면 계속해서 내구도가 하락

def solution(board, skill):
    answer = 0
    rn, cn = len(board), len(board[0])
    diff = [[0] * (cn+1) for i in range(rn+1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1 : degree = -degree
        diff[r1][c1] += degree
        diff[r1][c2 + 1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree
    for i in range(rn+1):
        d = diff[i][0]
        for j in range(1,cn+1):
            d += diff[i][j]
            diff[i][j] = d
    for i in range(cn+1):
        d = diff[0][i]
        for j in range(1,rn+1):
            d += diff[j][i]
            diff[j][i] = d
    for i in range(rn):
        for j in range(cn):
            board[i][j] += diff[i][j]
            if board[i][j] > 0 : answer += 1
    return answer