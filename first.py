﻿# coding: utf-8

import os
import sys
import shutil
import psutil

#

print("Hello world")
name = input("Your name: ")

print(name, ", welcome to Python!")

answer = ''
while answer != 'q':
    answer = input("Хочешь поработать? (y/n/q)")
    if answer == 'y':
        print("Отлично, хозяин!")
        print("Я умею:")
        print("  1 - вывести список файлов")
        print("  2 - вывести информацию о системе")
        print("  3 - вывести список процессов")
        print("  4 - продублировать файлы")
        print("  5 - дублировать определенный файл")
        print("  6 - удалить файлы .dupl")
        do = int(input("Что сделать? "))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Текущая директория: ", os.getcwd())
            print("Текущая платформа: ", sys.platform)
            print("Текущая кодировка ФС: ", sys.getfilesystemencoding())
            print("Текущий пользователь: ", os.getlogin())
            print("Количество процессоров: ", psutil.cpu_count())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("Дублируем файлы")
            file_list = os.listdir()
            print(os.listdir())
            # duplicate all files
            print(file_list)
            i = 0
            while i < len(file_list):
                print(file_list[i])
                if os.path.isfile(file_list[i]):
                    if file_list[i] != '.git':
                        newfile = file_list[i] + '.dupl'
                        shutil.copy(file_list[i], newfile)
                i += 1
        elif do == 5:
            print(os.listdir())
            file_name = input("Какой файл дублировать?")
            if os.path.isfile(file_name):
                newfile = file_name + '.dupl'
                shutil.copy(file_name, newfile)
        elif do == 6:
            dir_name = input('Укажите имя директории: ')
            file_list = os.listdir(dir_name)
            print(file_list)
            i = 0
            while i < len(file_list):
                longname = os.path.join(dir_name, file_list[i])
                if longname.endswith('.dupl'):
                    print('Удаляю: ' + longname)
                    os.remove(longname)
                i += 1
            print('Все файлы .dupl в директории ' + dir_name + ' удалены!')
        else:
            pass

    elif answer == 'n':
        print("Goodbye!")
    else:
        print("I don't know...")
