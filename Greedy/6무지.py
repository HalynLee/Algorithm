def solution(food_times, k):
    n = len(food_times)
    i, t = 0, 0  # i는 접시를 가리키는 수, t는 시간
    left = [1] * n

    while t < k:
        if food_times[i % n] > 0:
            food_times[i % n] -= 1
            t += 1
        if food_times[i % n] < 1:
            if left[i % n] == 1:
                left[i % n] = 0

        i += 1
        print('foodtimes ', end='')
        print(food_times)
        print('left      ', end='')
        print(left)

    if sum(food_times) < 1:
        return -1

    if left[(i+1)%n] == 1:
        return i%n + 2
    else:
        for i in range((i+1)%n, n):
            if left[(i+1)%n] == 0:
                continue
            else:
                return (i+2)%n


print(solution([6, 1, 1, 1, 2, 2, 2], 12))