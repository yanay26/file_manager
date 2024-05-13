import os
import shutil
from settings import WORKING_DIRECTORY

def create_folder(folder_name):
    """
    Создает новую папку в рабочей директории.

    :param folder_name: Имя новой папки.
    """
    # Полный путь к новой папке
    new_folder_path = os.path.join(WORKING_DIRECTORY, folder_name)

    try:
        # Создаем новую папку
        os.mkdir(new_folder_path)
        print(f"Папка '{folder_name}' успешно создана.")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует.")
    except Exception as e:
        print(f"Ошибка при создании папки '{folder_name}': {e}")



def delete_folder(folder_name):
    """
    Удаляет указанную папку из рабочей директории.

    :param folder_name: Имя папки для удаления.
    """
    # Полный путь к папке для удаления
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)

    try:
        # Удаляем папку
        os.rmdir(folder_path)
        print(f"Папка '{folder_name}' успешно удалена.")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не существует.")
    except OSError as e:
        print(f"Ошибка при удалении папки '{folder_name}': {e}")




def move_into_folder(folder_name):
    """
    Перемещается внутрь указанной папки.

    :param folder_name: Имя папки для перемещения.
    """
    global WORKING_DIRECTORY

    # Полный путь к целевой папке
    target_folder_path = os.path.join(WORKING_DIRECTORY, folder_name)

    # Проверяем, существует ли целевая папка
    if not os.path.exists(target_folder_path) or not os.path.isdir(target_folder_path):
        print(f"Папка '{folder_name}' не найдена.")
        return

    # Обновляем рабочую директорию
    WORKING_DIRECTORY = target_folder_path
    print(f"Перешли в папку '{folder_name}'.")



def move_up_folder():
    """
    Перемещается на уровень вверх.
    """
    global WORKING_DIRECTORY

    # Получаем родительскую папку
    parent_folder = os.path.dirname(WORKING_DIRECTORY)

    # Проверяем, не находимся ли мы уже в корневой папке
    if parent_folder == WORKING_DIRECTORY:
        print("Вы уже находитесь в корневой папке.")
        return

    # Обновляем рабочую директорию
    WORKING_DIRECTORY = parent_folder
    print("Перешли на уровень вверх.")



def create_empty_file(file_name):
    """
    Создает новый пустой файл в рабочей директории.

    :param file_name: Имя нового файла.
    """
    # Полный путь к новому файлу
    file_path = os.path.join(WORKING_DIRECTORY, file_name)

    try:
        # Создаем новый пустой файл
        with open(file_path, 'w'):
            pass
        print(f"Пустой файл '{file_name}' успешно создан.")
    except FileExistsError:
        print(f"Файл '{file_name}' уже существует.")
    except Exception as e:
        print(f"Ошибка при создании пустого файла '{file_name}': {e}")



def write_to_file(file_name, text):
    """
    Записывает текст в указанный файл.

    :param file_name: Имя файла для записи.
    :param text: Текст для записи в файл.
    """
    # Полный путь к файлу
    file_path = os.path.join(WORKING_DIRECTORY, file_name)

    try:
        # Открываем файл для записи (создаем его, если он не существует)
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Текст успешно записан в файл '{file_name}'.")
    except Exception as e:
        print(f"Ошибка при записи текста в файл '{file_name}': {e}")



def read_file(file_name):
    """
    Выводит содержимое указанного текстового файла.

    :param file_name: Имя файла для чтения.
    """
    # Полный путь к файлу
    file_path = os.path.join(WORKING_DIRECTORY, file_name)

    try:
        # Открываем файл для чтения
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Содержимое файла '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_name}': {e}")



def delete_file(file_name):
    """
    Удаляет указанный файл.

    :param file_name: Имя файла для удаления.
    """
    # Полный путь к файлу
    file_path = os.path.join(WORKING_DIRECTORY, file_name)

    try:
        # Удаляем файл
        os.remove(file_path)
        print(f"Файл '{file_name}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла '{file_name}': {e}")


def copy_file(source_file, destination_folder):
    """
    Копирует указанный файл из рабочей директории в указанную папку.

    :param source_file: Имя файла для копирования.
    :param destination_folder: Имя папки, в которую нужно скопировать файл.
    """
    # Полный путь к исходному файлу
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    # Полный путь к целевой папке
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder)

    try:
        # Проверяем, существует ли целевая папка, и создаем ее, если не существует
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Полный путь к целевому файлу
        destination_file_path = os.path.join(destination_path, source_file)

        # Копируем файл
        shutil.copy(source_path, destination_file_path)

        print(f"Файл '{source_file}' успешно скопирован в папку '{destination_folder}'.")
    except FileNotFoundError:
        print(f"Файл '{source_file}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла '{source_file}': {e}")



def move_file(source_file, destination_folder):
    """
    Перемещает указанный файл из рабочей директории в указанную папку.

    :param source_file: Имя файла для перемещения.
    :param destination_folder: Имя папки, в которую нужно переместить файл.
    """
    # Полный путь к исходному файлу
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    # Полный путь к целевой папке
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder)

    try:
        # Проверяем, существует ли целевая папка, и создаем ее, если не существует
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Полный путь к целевому файлу
        destination_file_path = os.path.join(destination_path, source_file)

        # Перемещаем файл
        shutil.move(source_path, destination_file_path)

        print(f"Файл '{source_file}' успешно перемещен в папку '{destination_folder}'.")
    except FileNotFoundError:
        print(f"Файл '{source_file}' не найден.")
    except Exception as e:
        print(f"Ошибка при перемещении файла '{source_file}': {e}")



def rename_file(old_name, new_name):
    """
    Переименовывает указанный файл.

    :param old_name: Старое имя файла.
    :param new_name: Новое имя файла.
    """
    # Полный путь к старому файлу
    old_path = os.path.join(WORKING_DIRECTORY, old_name)
    # Полный путь к новому файлу
    new_path = os.path.join(WORKING_DIRECTORY, new_name)

    try:
        # Переименовываем файл
        os.rename(old_path, new_path)
        print(f"Файл '{old_name}' успешно переименован в '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл '{old_name}' не найден.")
    except FileExistsError:
        print(f"Файл '{new_name}' уже существует.")
    except Exception as e:
        print(f"Ошибка при переименовании файла '{old_name}': {e}")


def main():
    while True:
        print("\nДоступные команды:")
        print("1. Создать папку")
        print("2. Удалить папку")
        print("3. Перейти в папку")
        print("4. Создать файл")
        print("5. Записать текст в файл")
        print("6. Просмотреть содержимое файла")
        print("7. Удалить файл")
        print("8. Копировать файл")
        print("9. Переместить файл")
        print("10. Переименовать файл")
        print("11. Выйти из программы")

        choice = input("Введите номер команды: ")

        if choice == "1":
            folder_name = input("Введите имя новой папки: ")
            create_folder(folder_name)
        elif choice == "2":
            folder_name = input("Введите имя папки для удаления: ")
            delete_folder(folder_name)
        elif choice == "3":
            folder_name = input("Введите имя папки для перехода: ")
            move_into_folder(folder_name)
        elif choice == "4":
            file_name = input("Введите имя нового файла: ")
            create_empty_file(file_name)
        elif choice == "5":
            file_name = input("Введите имя файла для записи текста: ")
            write_to_file(file_name)
        elif choice == "6":
            file_name = input("Введите имя файла для просмотра содержимого: ")
            read_file(file_name)
        elif choice == "7":
            file_name = input("Введите имя файла для удаления: ")
            delete_file(file_name)
        elif choice == "8":
            source_file = input("Введите имя файла для копирования: ")
            destination_folder = input("Введите имя папки для копирования: ")
            copy_file(source_file, destination_folder)
        elif choice == "9":
            source_file = input("Введите имя файла для перемещения: ")
            destination_folder = input("Введите имя папки для перемещения: ")
            move_file(source_file, destination_folder)
        elif choice == "10":
            old_name = input("Введите старое имя файла: ")
            new_name = input("Введите новое имя файла: ")
            rename_file(old_name, new_name)
        elif choice == "11":
            print("Программа завершена.")
            break
        else:
            print("Некорректная команда. Пожалуйста, выберите один из предложенных вариантов.")

if __name__ == "__main__":
    main()

