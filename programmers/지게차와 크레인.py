# 세로 n, 가로 m 둘다 최대 50 
# 전체 갯수 50 * 50 = 2500
# 접근 가능 컨테이너, 4면 중 1면이 외부와 연결
# 출고방법 100
# 전체탐색 100번 * 전체갯수2500 * 출고방법 100 = 25000000
move = [(0,-1),(0, 1),(1,0),(-1,0)]

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = n * m
    for i in range(len(storage)):
        storage[i] = list(storage[i])
        
    def dfs(y, x) :
        visited = [[True] * m for _ in range(n)]
        stack = [(y, x)]
        while stack :
            y, x = stack.pop()
            for i in move :
                move_y, move_x = i[0] + y, i[1] + x
                if (move_y < 0 or move_y >= n) or (move_x < 0 or move_x >= m) :
                    return True
                if visited[move_y][move_x] and storage[move_y][move_x] == " " :
                    visited[move_y][move_x] = False
                    stack.append((move_y, move_x))
                    
                    
        return False
    for i in requests : #최대 시행 횟수 : 100
        temp = []
        for y in range(n) : #최대 시행 횟수 : 50
            for x in range(m): #최대 시행 횟수 : 50
                if len(i) == 1 :
                    if storage[y][x] == i and dfs(y,x):
                        answer -= 1
                        temp.append((y,x))
                else :
                    if storage[y][x] == i[0] :
                        answer -= 1
                        temp.append((y,x))
        for j in temp :
            y, x = j
            storage[y][x] = " "
    return answer