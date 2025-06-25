# 칸토어집합은 0~1까지의 각 구간을 3등분한 후 가운데 구간을 제외하는 방식으로 풀이
# 3 ** n 개로 이루어진 -의 집합을 칸토어집합으로 풀이하는 문제
while True :
    try :
        n = int(input())
        arr = ["-"] * (3**n)
        def div(x, n):
            if n == 1 :
                return
            n = n // 3
            for i in range(x+n, x+(n*2)):
                arr[i] = " "
            div(x,n)
            div(x+(n*2),n)
        div(0,3**n)
        print("".join(arr))
    except :
        break