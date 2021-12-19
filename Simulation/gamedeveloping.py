n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 크기만큼 리스트 생성, 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1

# 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
fail = 0
num = 1

# 요구사항에 따라 전진하는 함수
while True:

    # 다음 턴 방향 전환
    direction = (direction - 1) % 4

    # 다음 턴 칸
    nx = x + moves[direction][0]
    ny = y + moves[direction][1]

    # 가보지 않았으면서 육지일 때
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 칸 이동
        x = nx
        y = ny

        # 맵 방문 처리
        d[x][y] = 1

        num += 1
        fail = 0
        continue

    else:
        fail += 1

    # 네 방향 다 갈 수 없는 경우
    if fail == 4:
        nx = x - moves[direction][0]
        ny = y - moves[direction][1]

        # 뒤로 갔을 때 육지일 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 바다일 경우
        else:
            break
        fail = 0

print(num)


