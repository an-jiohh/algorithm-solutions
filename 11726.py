width = int(input())
cache = [-1] * 1001

def tiling(width) :
    if width < 2 : return 1
    if cache[width] != -1 : return cache[width]
    cache[width] = (tiling(width-2) + tiling(width-1)) % 10007
    return cache[width]

print(tiling(width))