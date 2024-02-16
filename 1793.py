cache = [-1] * 251

def tiling(width) :
    if width < 2 : return 1
    if cache[width] != -1 : return cache[width]
    cache[width] = tiling(width-1) + tiling(width-2) + tiling(width-2)
    return cache[width]


while True :
    try :
        width = int(input())
        print(tiling(width))
    except :
        exit()