# 341이 어디인지 찾아야함
# 이후 좌표를 옮겨 해당 좌표에 어떤 값이 있는지 찾아야함

d, d_num = input().split()
dx, dy = map(int, input().split())

d = int(d)
x, y = 0, 0
size = 2 ** d

for i in range(d):
    size = size // 2
    target = d_num[i]

    if target == "1" :
        x += size
    elif target == "2" :
        pass
    elif target == "3" :
        y += size
    elif target == "4" :
        x += size
        y += size

x = dx + x
y = y - dy

answer, size = "", 2 ** d
if not 0 <= x < 2 **d or not 0 <= y < 2 ** d :
    answer = "-1"
else :
    for i in range(d):
        size = size // 2
        if  x >= size and y >= size :
            answer += "4"
            x -= size
            y -= size
        elif x >= size :
            answer += "1"
            x -= size
        elif y >= size :
            answer += "3"
            y -= size
        else :
            answer += "2"
print(answer)
