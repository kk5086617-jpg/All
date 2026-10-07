class NotLettersError(ValueError):
    pass


def get_only_letters(prompt):
    alphabet = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    )

    while True:
        try:
            user_input = input(prompt)

            if not user_input:
                raise NotLettersError("Строка не должна быть пустой!")

            for char in user_input:
                if char not in alphabet:
                    raise NotLettersError(
                        f"Обнаружен недопустимый символ: '{char}'"
                    )


            return user_input

        except NotLettersError as error:
            print(f"Ошибка ввода: {error}. Пожалуйста, повторите попытку.\n")


valid_string = get_only_letters("Введите слово (только буквы): ")
print(f"\nУспешно сохранено: {valid_string}")
