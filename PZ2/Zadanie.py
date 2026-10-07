import schedule
import time
import logging
import shutil
import os

# Настройка логирования в файл и вывод на экран одновременно
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("scheduler.log", encoding="utf-8"),
        logging.StreamHandler() # Чтобы статус дублировался в консоль
    ]
)

def run_task(operation, source, destination):
    """Выполнение файловой операции"""
    try:
        # Проверка существования источника (для всех операций кроме удаления)
        if not os.path.exists(source) and operation != 'delete':
            logging.error(f"Исходный путь не найден: {source}")
    

        if operation == 'copy':
            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)
            logging.info(f"Успешно скопировано: {source} -> {destination}")

        elif operation == 'move':
            shutil.move(source, destination)
            logging.info(f"Успешно перемещено: {source} -> {destination}")

        elif operation == 'delete':
            if os.path.exists(source):
                if os.path.isdir(source):
                    shutil.rmtree(source)
                else:
                    os.remove(source)
                logging.info(f"Успешно удалено: {source}")
            else:
                logging.info(f"Пропущено: Файл/папка для удаления не существовали: {source}")

        elif operation == 'archive':
            base_dir = os.path.dirname(source)
            base_name = os.path.basename(source)
            # Создает zip-архив (расширение .zip добавится автоматически)
            shutil.make_archive(destination, 'zip', base_dir, base_name)
            logging.info(f"Успешно создан архив: {destination}.zip из {source}")

    except Exception as e:
        logging.error(f"Ошибка при выполнении операции {operation}: {e}")

def main():
    print("=== файловый планировщик ===")
    
    # 1. Сбор параметров
    print("Доступные операции: copy (копировать), move (переместить), delete (удалить), archive (архивировать)")
    operation = input("Введите операцию: ").strip().lower()
    if operation not in ['copy', 'move', 'delete', 'archive']:
        print("Неверная операция! Выход.")
        return

    source = input("Введите путь к исходному файлу/папке: ").strip()
    
    destination = None
    if operation in ['copy', 'move', 'archive']:
        destination = input("Введите путь назначения (для архива — имя файла без .zip): ").strip()

    time_str = input("Введите время ежедневного запуска (например, 14:30): ").strip()

    # 2. Планирование задачи
    schedule.every().day.at(time_str).do(run_task, operation, source, destination)
    
    logging.info(f"Задача [{operation.upper()}] успешно запланирована на каждый день в {time_str}")
    print("Не закрывайте это окно. Для выхода нажмите Ctrl+C\n")

    # 3. Ожидание времени запуска
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")

if __name__ == "__main__":
    main()
