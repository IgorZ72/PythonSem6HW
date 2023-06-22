from random import randint
random_list = [randint(-5, 15) for i in range(30)]
print(random_list)
min = int(input('введите мин число: '))
max = int(input('введите макс число: '))
for i in range(len(random_list)):
    if min <= random_list[i] <= max:
        print(i, end=' ')

