
def change(key): #회전
    n = len(key)
    new_key = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][n-i-1] = key[i][j]
    return new_key

def check(key, lock):
    m,n = len(key), len(lock)
    board_size = m + 2 * n - 2
    board = [[0] * board_size for _ in range(board_size)]
    offset = m-1
    for i in range(n):
        for j in range(n):
            board[offset+i][offset+j] = lock[i][j]
    for i in range(board_size-m+1):
        for j in range(board_size-m+1):
            check_board = [row[:] for row in board]
            for y in range(m):
                for x in range(m):
                    check_board[y+i][x+j] += key[y][x]
            check = True
            for y in range(n):
                for x in range(n):
                    if check_board[offset+y][offset+x] != 1:
                        check = False
            if check : return True

def solution(key, lock):
    for i in range(4):
        if check(key,lock) :
            return True
        key = change(key)
    return False
