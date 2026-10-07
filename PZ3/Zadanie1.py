print("-----------------------------------")


while True:
    try:
        heigh = int(input("Введите ваш рост в см: "))
        weight = int(input("Введите ваш вес в кг: "))
        
        if weight <= 0 or heigh <= 0:
            print("некоректный ввод\n")
            continue
            
        break
        
    except ValueError:
        print("Ошибка: Нужно вводить только целые числа! Попробуйте снова.\n")

normal_weight = heigh - 100
if weight >= normal_weight:
    if weight == normal_weight:
        print("Чотка")
    else:
        print("Худей")
else:
    print("Толстей")
print("---------------------------------------------");
