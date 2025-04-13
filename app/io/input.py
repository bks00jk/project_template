import pandas as pd
import os

def read_from_console():
    """
    Зчитує текст, введений користувачем через консоль.

    Returns:
        str: Текст, введений користувачем.
    """
    try:
        return input("Введіть текст у консолі: ")
    except KeyboardInterrupt:
        return "Введення перервано користувачем."

def read_from_file():
    """
    Зчитує дані з файлу за допомогою вбудованих можливостей Python.

    Returns:
        str: Вміст файлу у вигляді рядка.
    """
    file_path = os.path.join("data", "input_file.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        return f"Помилка: Файл {file_path} не знайдено."
    except Exception as e:
        return f"Помилка при зчитуванні файлу: {str(e)}"

def read_with_pandas():
    """
    Зчитує дані з файлу за допомогою бібліотеки pandas.

    Returns:
        pandas.DataFrame: Дані з файлу у вигляді DataFrame.
    """
    file_path = os.path.join("data", "input_file.csv")
    try:
        df = pd.read_csv(file_path)
        return df.to_string(index=False)
    except FileNotFoundError:
        return f"Помилка: Файл {file_path} не знайдено."
    except pd.errors.EmptyDataError:
        return "Помилка: Файл порожній."
    except Exception as e:
        return f"Помилка при зчитуванні за допомогою pandas: {str(e)}"