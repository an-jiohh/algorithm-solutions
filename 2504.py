st = list(input())

stack = []

for i in st :
    if i == "[" or i == "(":
        stack.append(i)
    if i == "]" or i == ")":
        temp_list = []
        if not stack :
            print(0)
            exit(0)
        while stack :
            temp = stack.pop()
            if isinstance(temp, int) and stack :
                temp_list.append(temp)
            elif temp == "[" and i == "]":
                point = sum(temp_list) * 3
                stack.append(max(point, 3))
                break
            elif temp == "(" and i == ")" :
                point = sum(temp_list) * 2
                stack.append(max(point, 2))
                break
            else :
                print(0)
                exit(0)

try : print(sum(stack))
except :print(0)