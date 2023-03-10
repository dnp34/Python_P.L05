# Main Menu
# from PIL import Image, ImageFont, ImageDraw
from famous_people import quiz
from get_requests import get_ip, send_photo
from info import print_logo
from os_info import os_info
from personal_bank import my_bank
from file_tools import *


menu = {'11': 'информация о системе',
        '21': 'создать папку',
        '22': 'удалить (файл/папку)',
        '23': 'копировать (файл/папку)',
        '24': 'просмотр содержимого директории',
        '25': 'посмотреть только папки',
        '26': 'посмотреть только файлы',
        '27': 'смена рабочей директории',
        '31': 'играть в викторину',
        '32': 'мой банковский счет',
        '33': 'информация по ip-адресу',
        '34': 'справка Markdown (смс на Telegram)',
        '35': 'создатель программы (Info)',
        '00': 'выход.'
        }


def stop_menu():
    print('😎 До скорой встречи!')
    return False


def print_menu():
    title = ' МЕНЮ '
    max_str = int((max((len(v)) for v in menu.values()) + 4 - len(title)) / 2)
    print('\n', '=' * max_str, title, '=' * max_str)
    for key, val in menu.items():
        print(f'{key}. {val}')
    print('-' * (max_str * 2 + len(title) + 2))
    return


def start_menu(ask=True):
    while ask:
        print_menu()
        item = input('... Ваш выбор: ')
        if item in menu.keys():
            if item == "00":
                ask = stop_menu()
            elif item == "11":
                os_info()
            elif item == "21":
                mk_dir(input('\nВведите новую папку для создания: '))
            elif item == "22":
                rm_dir(input('\nВведите папку или файл для удаления: '))
            elif item == "23":
                p1 = input('\nВведите файл/папку для копирования: ')
                p2 = input('Введите файл/папку назначения: ')
                file_copy(p1, p2)
            elif item == "24":
                list_all()
            elif item == "25":
                list_dir()
            elif item == "26":
                list_files()
            elif item == "27":
                change_dir(input('\nВведите новую рабочую директорию: '))
            elif item == "31":
                quiz()
            elif item == "32":
                my_bank()
            elif item == "33":
                get_ip()
            elif item == "34":
                send_photo()
            elif item == "35":
                print_logo()
            else:
                print('Ok')
        else:
            print(' 🚫 Ошибка выбора пункта меню!')
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
