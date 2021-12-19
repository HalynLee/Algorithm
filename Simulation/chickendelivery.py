from itertools import combinations

n, m = map(int, input().split())

# 맵 정보 입력받기
array = []
chicken = []
house = []
chicken_num = 0

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chicken.append((i, j))
            chicken_num += 1
        elif array[i][j] == 1:
            house.append((i, j))

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

cdistance = 0
result = []
total = []

if chicken_num == m : # 폐업할 가게가 없으면
    for h in house:
        for c in chicken:
            result.append(distance(h, c))
        cdistance += min(result)
        result = []
    print(cdistance)

else:
    cand = list(combinations(chicken, m)) # 살아남을 치킨집 조합 추출
    for stores in cand:
        for h in house:
            for c in stores:
                result.append(distance(h, c))
            cdistance += min(result)
            result = []
        total.append(cdistance)
        cdistance = 0

    print(min(total))