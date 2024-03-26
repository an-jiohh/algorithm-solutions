arr = input()
score = {"+":1,"-":1,"*":2,"/":2,"(":0}
stack = []
answer = []
for i in arr :
    if i.isalpha() : answer.append(i)
    else :
        if i == "(" : 
            stack.append(i)
            continue
        while stack :
            if i == ")" :
                temp = stack.pop()
                if temp != "(" : answer.append(temp)
                else : break
            elif score[stack[-1]] < score[i] :
                stack.append(i)
                break
            elif score[stack[-1]] >= score[i] :
                temp = stack.pop()
                answer.append(temp)
        else :
            stack.append(i)
while stack :
    answer.append(stack.pop())
print("".join(answer))