
correct_year = 1893

user_answer = int(input("В каком году был основан Новосибирск? "))

# Проверка ответа
if user_answer == correct_year:
    print("Правильно!")
else:
    print(f"Неверно. Правильный ответ: Новосибирск был основан в {correct_year} году.")
