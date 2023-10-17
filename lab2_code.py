print('Флаг Бенина:')
print(u"\u001b[42m      \u001b[43m         \u001b[0m")
print(u"\u001b[42m      \u001b[43m         \u001b[0m")
print(u"\u001b[42m      \u001b[41m         \u001b[0m")
print(u"\u001b[42m      \u001b[41m         \u001b[0m")
print()

print('Узор h:')
x = u"\u001b[42m \u001b[0m"
k = 5
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
print()

print('График функции y = x + 1:')
print('↑y')
for y in range(10, 0, -1):
    x = y - 1
    print('|' + ' ' * x + '/')
print('|', end='')
print('-' * 10 + '→')
print('0' + ' ' * 15 + 'x')
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
percent1 = round(x1 / cnt * 100)
percent2 = round(x2 / cnt * 100)
x = u"\u001b[42m \u001b[0m"
y = u"\u001b[41m \u001b[0m"
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
