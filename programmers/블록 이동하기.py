from collections import deque

dm = [(1,0),(-1,0),(0,1),(0,-1)]

d = [(0,1),(1,0),(0,-1),(-1,0)]
d_check = [[(),(1,1),(),(-1,1)],[(1,1),(),(1,-1),()],[(),(1,-1),(),(-1,-1)],[(-1,1),(),(-1,-1),()]]
d_change = [2,3,0,1]

def solution(board):
    n = len(board)
    answer = 0
    queue = deque([[0,0,0,0]]) #y, x, position, count
    
    visited = set()
    visited.add((0,0,0))
    while queue:
        y,x,position,count = queue.popleft()
        check_y, check_x = y+d[position][0], x+d[position][1]
        if (y == n-1 and x == n-1) or (check_y == n-1 and check_x == n-1) :
            return count
            
        for my, mx in dm :
            my1, mx1 = y + my, x + mx
            my2, mx2 = y + my + d[position][0], x + mx + d[position][1]
            if 0 <= my1 < n and 0 <= mx1 < n and 0 <= my2 < n and 0 <= mx2 < n :
                if board[my1][mx1] == 0 and board[my2][mx2] == 0 :
                    state = (my1, mx1, position)
                    if state not in visited:
                        visited.add(state)
                        queue.append((my1,mx1,position,count+1))
                    
        temp_position = position + 1
        if temp_position == 4 : temp_position = 0
        my, mx = d[temp_position]
        my, mx = y + my, x + mx
        cy, cx = d_check[position][temp_position]
        cy, cx = y + cy, x + cx
        if 0 <= my < n and 0 <= mx < n and 0 <= cx < n and 0 <= cy < n :
            if board[my][mx] == 0 and board[cy][cx] == 0:
                state = (y, x, temp_position)
                if state not in visited:
                    visited.add(state)
                    queue.append((y,x,temp_position, count+1))
        
        temp_position = position - 1
        if temp_position == -1 : temp_position = 3
        my, mx = d[temp_position]
        my, mx = y + my, x + mx
        cy, cx = d_check[position][temp_position]
        cy, cx = y + cy, x + cx
        if 0 <= my < n and 0 <= mx < n and 0 <= cx < n and 0 <= cy < n :
            if board[my][mx] == 0 and board[cy][cx] == 0:
                state = (y, x, temp_position)
                if state not in visited:
                    visited.add(state)
                    queue.append((y,x,temp_position, count+1))
        
        temp_position = d_change[position] + 1 #반대편 기준으로 변경할 방향 설정
        if temp_position == 4 : temp_position = 0
        oy, ox = y + d[position][0], x + d[position][1]       # 축: 반대편 칸 (고정)
        my, mx = oy + d[temp_position][0], ox + d[temp_position][1]  # 축에서 새로 뻗는 칸

        # my, mx = d[position] #my, mx에 반대좌표 설정
        # my, mx = y + my, x+mx #my, mx에 반대좌표 설정
        # my, mx = my + d[temp_position][0], mx + d[temp_position][1]
        cy, cx = d_check[d_change[position]][temp_position]
        cy, cx = oy + cy, ox + cx
        if 0 <= my < n and 0 <= mx < n and 0 <= cx < n and 0 <= cy < n :
            if board[my][mx] == 0 and board[cy][cx] == 0:
                state = (oy, ox, temp_position)
                if state not in visited:
                    visited.add(state)
                    queue.append((oy,ox,temp_position, count+1))

        temp_position = d_change[position] - 1 #반대편 기준으로 변경할 방향 설정
        if temp_position == -1 : temp_position = 3
        oy, ox = y + d[position][0], x + d[position][1]       # 축: 반대편 칸 (고정)
        my, mx = oy + d[temp_position][0], ox + d[temp_position][1]
        # my, mx = d[position] #my, mx에 반대좌표 설정
        # my, mx = y + my, x+mx #my, mx에 반대좌표 설정
        # my, mx = my + d[temp_position][0], mx + d[temp_position][1]
        cy, cx = d_check[d_change[position]][temp_position]
        cy, cx = oy + cy, ox + cx
        if 0 <= my < n and 0 <= mx < n and 0 <= cx < n and 0 <= cy < n :
            if board[my][mx] == 0 and board[cy][cx] == 0:
                state = (oy, ox, temp_position)
                if state not in visited:
                    visited.add(state)
                    queue.append((oy,ox,temp_position, count+1))
    return 0