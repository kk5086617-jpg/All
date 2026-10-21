def find_fibonacci_index(n):
    """
    Находит порядковый номер K для заданного числа Фибоначчи N.
    """
    # Начальные значения для F_1 = 1 и F_2 = 1
    f_prev = 1
    f_curr = 1
    k = 2  # Текущий номер числа f_curr
    
    # Генерируем числа Фибоначчи, пока не дойдем до N
    while f_curr < n:
        # Считаем следующее число Фибоначчи
        f_next = f_prev + f_curr
        # Сдвигаем значения для следующего шага
        f_prev = f_curr
        f_curr = f_next
        # Увеличиваем порядковый номер
        k += 1
        
    return k

# --- Демонстрация работы ---
if __name__ == "__main__":
    # Запрашиваем у пользователя число N
    try:
        user_input = int(input("Введите число Фибоначчи N (> 1): "))
        
        if user_input <= 1:
            print("Ошибка: число должно быть строго больше 1.")
        else:
            result_k = find_fibonacci_index(user_input)
            print(f"Порядковый номер K для числа N = {user_input} равен: {result_k}")
            
    except ValueError:
        print("Ошибка: введено не целое число.")
