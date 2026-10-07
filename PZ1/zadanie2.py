def read_file(file_name):
    file = None
    try:
        file = open(file_name, "r") 

        for i in range(5):
            line = file.readline()
            if not line:
                break
            print(
                line, end=""
            ) 

    except FileNotFoundError:  
        print(f"Ошибка: файл '{file_name}' не найден.")
    except IOError:
        print("Ошибка: проблема с чтением файла.")
    finally:
        if file is not None:
            file.close()  
            print("\nФайл закрыт.") 



if __name__ == "__main__":
    read_file("text.txt") 
