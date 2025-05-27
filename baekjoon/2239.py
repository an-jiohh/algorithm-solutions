#스도쿠를 어떻게 푸는지 고민해보자
#숫자를 대입해보고, 가로확인, 세로확인, 3*3사각형 확인해서 다음으로 넘어감
#모든 값이 0이고 모든 값을 테스트할 경우의 수를 구해보면
# 한칸에 9숫자
# 가로 확인 9, 세로확인 9, 중간확인 9 -> 27
# 81개의 칸이므로 
# 27 * 9 ** 81 -> 9**81 = ???
# 최적화가 필수가됨 => 백트래킹?
 
arr = [list(map(int, list(input()))) for _ in range(9)]
check_row = [[True]*10 for _ in range(10)]
check_col = [[True]*10 for _ in range(10)]
check_box = [[[True]*10 for _ in range(3)] for __ in range(3)]

def checking(y,x,num):
    check_row[y][num] = False #가로체크
    check_col[x][num] = False #세로체크
    check_box[y//3][x//3][num] = False #작은 사각형 체크

def unchecking(y,x,num):
    check_row[y][num] = True #가로체크
    check_col[x][num] = True #세로체크
    check_box[y//3][x//3][num] = True #작은 사각형 체크

zero = []
for y in range(9):
    for x in range(9):
         num = arr[y][x]
         if num == 0 :
             zero.append((y,x))
             continue
         checking(y,x,num)

def dfs(y, x):
    if y == 9 and x == 0 :
        for row in arr:
            print(*row, sep="")
        exit(0)
        return
    if arr[y][x] == 0 :
        for i in range(1,10):
            if check_row[y][i] and check_col[x][i] and check_box[y//3][x//3][i] :
                arr[y][x] = i
                checking(y, x, i)
                next_x, next_y = x + 1, y
                if next_x == 9 : 
                    next_x, next_y = 0, next_y + 1
                dfs(next_y, next_x)
                unchecking(y, x, i)
                arr[y][x] = 0
    else :
        next_x, next_y = x + 1, y
        if next_x == 9 : 
            next_x, next_y = 0, next_y + 1
        dfs(next_y, next_x)

dfs(0,0)
print(arr)