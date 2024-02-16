arr = input().split("-")
round = []
for i in arr :
    sub = list(map(int, i.split("+")))
    round.append(sum(sub))

sum = round[0]
for i in round[1:] :
    sum -= i

print(sum)