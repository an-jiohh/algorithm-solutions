# moo 패턴을 이용해서 계속해서 만들 수 있긴함
# 근데 몇번쨰까지 만들어야 n번째 글자까지 만들 수 있을지 모르겠음
N = int(input())

length = [3]

while length[-1] < N :
    length.append(length[-1] + len(length) + 3 + length[-1])

def find(n, k):
    if k == 0 :
        if n == 1 : return 'm'
        else : return "o"
    
    left = length[k-1]
    center = k+3

    if n <= left :
        return find(n, k-1)
    elif n <= left + center :
        if n-left == 1 :
            return 'm'
        else :
            return 'o'
    else :
        return find(n-left-center,k-1)
        
print(find(N, len(length)-1))