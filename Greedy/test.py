food_times = [0,0,1]
n = 3

i = 0

if food_times[i % n] > 0:
    food_times[i % n] -= 1
    i += 1
else:
    print('it is less than 1')
