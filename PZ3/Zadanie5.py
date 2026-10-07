print("--------------------------------")
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка: Нужно вводить только целые числа! Попробуйте снова.\n")

print("--------------------------------")

if number % 2 == 0:
    print(f"Число {number} — чётное.")
else:
    print(f"Число {number} — нечётное.")

print("--------------------------------")
