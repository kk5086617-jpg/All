# функция для проверки едят ферзи друг друга или нет
def threat(q1, q2):
    x1, y1 = q1
    x2, y2 = q2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

# ввод координат трех ферзей
queens = []
for i in range(1, 4):
    print(f"Введите координаты {i}-го ферзя (через пробел, от 1 до 8):")
    x, y = map(int, input().split())
    queens.append((x, y))

# проверка всех пар
found_pairs = False

# пары: (1 и 2), (1 и 3), (2 и 3)
pairs = [(0, 1), (0, 2), (1, 2)]

for i, j in pairs:
    if threat(queens[i], queens[j]):
        print(f"Ферзь {i+1} {queens[i]} и Ферзь {j+1} {queens[j]} угрожают друг другу.")
        found_pairs = True

if not found_pairs:
    print("Ни один ферзь не угрожает другому.")
