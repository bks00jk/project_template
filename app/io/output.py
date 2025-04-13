import os

def write_to_console(text):
    """
    Виводить текст у консоль.

    Args:
        text (str): Текст для виведення у консоль.
    """
    print("Результат у консолі:")
    print(text)

def write_to_file(text, file_path):
    """
    Записує текст до файлу за допомогою вбудованих можливостей Python.

    Args:
        text (str): Текст для запису у файл.
        file_path (str): Шлях до файлу, куди буде виконано запис.
    """
    try:
        full_path = os.path.join("data", file_path)
        with open(full_path, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except Exception as e:
        print(f"Помилка при записі до файлу {full_path}: {str(e)}")