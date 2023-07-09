# program accomplished by alsam2009
# https://github.com/alsam2009

# Документация по os.walk():
# https://docs.python.org/3/library/os.html#os.walk

import os
import csv

# TODO:  add try/catch

# Получатель всех подкаталогов в корне
def get_dirs_files(path):
    files_in_course = [] # накопитель файлов путей подкаталогов в корневом каталоге
    files_output = "dirs_in_root.csv" # наименование выходного файла с результатом работы
    for root, dirs, files in os.walk(path):
        # print(dirs) if dirs else None # выводит в консоль все пути каталогов
        # print(files) if files else None # выводит в консоль все файлы каталога и подкаталогов. Возвращает list []
        files_in_course.append([root])  # добавляет директории и пути к ним в list
    with open(
        files_output,
        "w",
        newline="",
    ) as f:  # записывает все директории и пути к ним начиная с рабочей директории (path)
        csv.writer(f, delimiter=";").writerows(files_in_course)

        # for file in files:
        #     if(file.endswith(".mp4")):
        #         files_in_course.append(os.path.join(root,file))
        #         # print(os.path.join(root,file))
    print(f'Готово! Проверьте файл {files_output}')

# Пакетный ренейминг файлов
def rename_files(path, pattern):
    print(f'\nНачал работу по адресу {path}...')
    # pattern = "[SW.BAND] " # "[SW.BAND] " - шаблон обрезки: что нужно убрать в наименованиях файлов и папок
    for root, _, files in os.walk(path):
        if pattern in root:
            os.rename(
                    root, root.replace(pattern, '')
                )
        for file in files:
            # print(file)
            if file.startswith(
                pattern
            ):
                os.rename(
                    os.path.join(root, file), os.path.join(root, file[10:])
                )  # обрезка наименования файла с 10 символа, т.е. сколько символов в шаблоне обрезки

    #     if(file.endswith(".mp4")):
    #         files_in_course.append(os.path.join(root,file))


def main():
    # path = r"E:\Курсы\Прочее\1. DOCKER" # путь до коревого каталога
    while True:
        desire_user = input(
            '\nPress key:\n----------\n[1] Get all dirs in root => csv output\n[2] Delete pattern in all dirs & files names in root\n[3] Exit\n')

        match desire_user:
            case "1":
                path = input('Paste root dir here: ')
                get_dirs_files(path)
            case "2":
                path = input('Paste root dir here: ')
                pattern = input('Paste pattern here (eg.: [SW.BAND]): ')
                rename_files(path,pattern)  # переименовывает все файлы в каталоге (path) и подкаталогах, убирает ненужный паттерн в наименовании файлов
            case "3":
                print('Goodbye!')
                break


if __name__ == "__main__":
    welcom = "*** ПАКЕТНЫЙ ПЕРЕИМЕНОВАТЕЛЬ ФАЙЛОВ ***"
    print(f'\n{welcom}\n{"_"*len(welcom)}')
    main()
