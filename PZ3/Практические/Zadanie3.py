print("--------------------------------")
while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        c = float(input("Введите число c: "))
        break
    except ValueError:
        print("Ошибка: Нужно вводить только числа! Попробуйте снова.\n")

print("--------------------------------")


numbers = [a, b, c]
result = []

for num in numbers:
    if num == 1.0:
        result.append(2.0)
    elif num % 2 == 0:
        result.append(num / 2)
    else:
        result.append(num)

print(f"Результат обработки: a = {result[0]}, b = {result[1]}, c = {result[2]}")
print("--------------------------------")



    