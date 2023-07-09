# program accomplished by alsam2009
# https://github.com/alsam2009

# Документация по os.walk():
# https://docs.python.org/3/library/os.html#os.walk

import os
import csv

# TODO:  add try/catch

# Получатель всех подкаталогов в корне


def get_dirs_files(path):
    files_in_course = []  # накопитель файлов путей подкаталогов в корневом каталоге
    # наименование выходного файла с результатом работы
    files_output = "dirs_in_root.csv"
    for root, dirs, files in os.walk(path):
        # print(dirs) if dirs else None # выводит в консоль все пути каталогов
        # print(files) if files else None # выводит в консоль все файлы каталога и подкаталогов. Возвращает list []
        # добавляет директории и пути к ним в list
        files_in_course.append([root])
    # записывает все директории и пути к ним начиная с рабочей директории (path)
    with open(files_output, "w", newline="",) as f:
        csv.writer(f, delimiter=";").writerows(files_in_course)

        # for file in files:
        #     if(file.endswith(".mp4")):
        #         files_in_course.append(os.path.join(root,file))
        #         # print(os.path.join(root,file))
    print(f'Done! Check a file: {files_output}')

# Пакетный ренейминг файлов


def rename_files(path, pattern):
    print(f'\nStarting on {path}')
    # pattern = "[SW.BAND] " # "[SW.BAND] " - шаблон обрезки: что нужно убрать в наименованиях файлов и папок
    for root, _, files in os.walk(path):
        for file in files:
            if file.startswith(pattern):
                # обрезка наименования файла с 10 символа, т.е. сколько символов в шаблоне обрезки
                os.rename(os.path.join(root, file), os.path.join(
                    root, file[len(pattern):]))
    for root, _, files in os.walk(path):
        if pattern in root:
            os.rename(root, root.replace(pattern, ''))
    #     if(file.endswith(".mp4")):
    #         files_in_course.append(os.path.join(root,file))
    print('Done!')


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
                # переименовывает все файлы в каталоге (path) и подкаталогах, убирает ненужный паттерн в наименовании файлов
                rename_files(path, pattern)
            case "3":
                print('Goodbye!')
                break


if __name__ == "__main__":
    welcom = "*** ПАКЕТНЫЙ ПЕРЕИМЕНОВАТЕЛЬ ФАЙЛОВ ***"
    print(f'\n{welcom}\n{"_"*len(welcom)}')
    main()
