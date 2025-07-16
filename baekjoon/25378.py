# 한줄로 N 장소에 각각 조약돌 몇개
# 두 장소에서 임의의 동일한 개수 가져가기
# 한 장소에서 임의의 개수 가져가기
# 조약돌을 다 가져가도 장소는 그대로 남아있음
# 모든 조약돌을 최소작업으로 가져가는 최소작업

N = int(input())

stone = list(map(int, input().split()))

stone_cnt = [[stone[i]] for i in range(N)]
cnt = N 

for i in range(1, N):
    for sc in stone_cnt[i-1]:
        if sc < stone[i]:
            stone_cnt[i].append(stone[i] - sc)
        elif sc == stone[i]:
            stone_cnt[i] = []
            cnt -= 1
            break
print(cnt)
