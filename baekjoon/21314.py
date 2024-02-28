string = input()

stack = []

mini = ""
maxi = ""

for i in string :
    if i == "K" :
        if stack :
            mini += str(10 ** (len(stack) - 1)) + "5"
        else :
            mini += "5"
        maxi += str((10 ** len(stack))*5)
        stack = []
    elif i == "M" :
        stack.append("M")

maxi += len(stack) * "1"
if stack : mini += str(10 ** (len(stack)-1))

print(maxi)
print(mini)