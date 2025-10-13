#작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태
#()두개의 개수가 같다면 균형잡힌 괄호 문자열
#짝도 모두 맞을때 올바른 괄호 문자열

def find(w):
    count = 0
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        elif w[i]== ")":
            count -= 1
        if count == 0:
            return i
def check(u):
    count = 0
    for i in range(len(u)):
        if u[i] == "(":
            count += 1
        elif u[i] == ")":
            count -= 1
        if count < 0 :
            return False
    if count == 0 : return True
    return False

def change(w):
    if w == "" : return w
    i = find(w)
    u, v = w[:i+1], w[i+1:]
    if check(u) : 
        v = change(v)
        return u + v
    temp = "("
    temp += change(v)
    temp += ")"
    for i in u[1:-1] :
        if i == "(" : 
            temp += ")"
        else : 
            temp += "("
    return temp

def solution(p):
    return change(p)