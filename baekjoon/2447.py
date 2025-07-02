n = int(input())
board = [[" "] * (n) for i in range(n)]

def split_qube(start_y, start_x, n):
    if n == 1  :
        board[start_y][start_x] = "*"
        return
    n = n // 3

    split_qube(start_y, start_x, n)
    split_qube(start_y, start_x+n, n)
    split_qube(start_y, start_x+(n*2), n)

    split_qube(start_y + n, start_x, n)
    split_qube(start_y + n, start_x + (2 * n), n)

    split_qube(start_y + (n*2), start_x, n)
    split_qube(start_y + (n*2), start_x+n, n)
    split_qube(start_y + (n*2), start_x+(n*2), n)

split_qube(0,0,n)

for row in board :
    print("".join(row))