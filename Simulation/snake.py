# 백준 3190
n = int(input())
k = int(input())

# 보드 초기화
board = [[0]*(n+1) for _ in range(n+1)]

# 사과 정보 입력받기
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

times = []
l = int(input())

for _ in range(l):
    x, c = input().split() ##
    times.append((int(x), c))

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # RDLU 순으로
# 현재 방향 d, 현재 머리 위치 hx, hy, 현재 꼬리 위치 tx, ty

d = 0
hx, hy, tx, ty = 1, 1, 1, 1
body = [(1,1)]

count = 0
nx, ny = 1, 1
while True:
    for time in times:
        if time[0] == count:
            # 방향 변환
            if time[1] == 'L':
                d = (d-1)%4
            else:
                d = (d+1)%4

    nx = hx + moves[d][0]
    ny = hy + moves[d][1]

    if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 2: # 머리가 이동했을 때 보드 밖일 경우
        count += 1
        break
    else:
        if board[nx][ny] == 1 : # 사과가 있을 경우

            body.append((nx,ny))
            board[nx][ny] = 2

        else: # 사과가 없을 경우
            board[nx][ny] = 2
            body.append((nx, ny))
            px, py = body.pop(0)
            board[px][py] = 0

        hx, hy = nx, ny
        count += 1

print(count)