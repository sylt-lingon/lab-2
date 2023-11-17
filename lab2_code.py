WIDTH_GR = 6
WIDTH_YR = 9
RED = 41
YELLOW = 43
GREEN = 42


def flag(color):
    print(f"\u001b[{GREEN}m{' '*WIDTH_GR}\u001b[0m", end='')
    print(f"\u001b[{color}m{' '*WIDTH_YR}\u001b[0m")


def pattern(color, k):
    x = f"\u001b[{color}m \u001b[0m"
    for i in range(1, 4):
        for j in range(k):
            print(' ' * (4 - i) + x * (2 * i - 1) + ' ' * (4 - i - 1), end='')
        print()
    for i in range(4, 0, -1):
        if i == 4:
            print(x * (6 * k + 1))
        else:
            for j in range(k):
                print(' ' * (4 - i) + x * (2 * i - 1) + ' ' * (4 - i - 1), end='')
            print()


def create_func(height, width):
    print('↑y')
    for y in range(height, 0, -1):
        x = y - 1
        print('|' + ' ' * x + '/')
    print('|', end='')
    print('-' * height + '→')
    print('0' + ' ' * width + 'x')


def count_percent(x, cnt):
    return round(x / cnt * 100)


def create_diagram(percent1, percent2, color1, color2):
    x = f"\u001b[{color1}m \u001b[0m"
    y = f"\u001b[{color2}m \u001b[0m"
    print('↑ percent, %')
    for i in range(100, 0, -1):
        if percent1 >= i and percent2 >= i:
            print('|' + x + y)
        elif percent1 >= i:
            print('|' + x)
        elif percent2 >= i:
            print('|' + ' ' + y)
        else:
            print('|')
    print('|' + '-' * 3 + '→')
    print('0')


print('Флаг Бенина:')
for i in range(2):
    flag(YELLOW)
for i in range(2):
    flag(RED)
print()

print('Узор h:')
pattern(GREEN, 5)
print()

print('График функции y = x + 1:')
create_func(10, 15)
print()

print('Диаграмма процентного соотношения чисел от 0 до 5 и от 0 до -5:')
with open('sequence.txt') as f:
    x1 = 0
    x2 = 0
    cnt = 0
    for line in f:
        s = float(line)
        cnt += 1
        if 0 <= s <= 5:
            x1 += 1
        elif -5 <= s <= 0:
            x2 += 1
percent1 = count_percent(x1, cnt)
percent2 = count_percent(x2, cnt)
create_diagram(percent1, percent2, GREEN, RED)
