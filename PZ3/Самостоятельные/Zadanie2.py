
x = float(input("Введите x: "))
y = float(input("Введите y: "))


inside_rhomb = abs(x) + abs(y) <= 5
outside_circle = (x**2 + y**2) >= 9

if inside_rhomb and outside_circle:
    print("Точка принадлежит заштрихованной области")
else:
    print("Точка не принадлежит заштрихованной области")
