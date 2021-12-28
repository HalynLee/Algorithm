n, m = map(int, input().split())

data = []
temp = [[0]*m for _ in range(n)] # 벽 설치 후의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS로 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메소드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기를 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 바이러스 전파 후 공간 안전 영역 카운트 계산해서 리턴
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0: # 빈 공간일 경우
                data[i][j] = 1 # 울타리 설치
                count += 1 # 카운트 증가
                dfs(count) # 울타리 설치
                data[i][j] = 0 # 울타리 설치 취소하고
                count -= 1 # 카운트 마이너스


dfs(0)
print(result)
