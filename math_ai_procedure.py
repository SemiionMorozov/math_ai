# Экспериментальная модель машинного обучения - на примере простых операций с числами (умный калькулятор)
# 24.02.2019 - Semion Morozov - semiion-morozov@mail.ru

a = int(input('Введите число a = '))
b = int(input('Введите число b = '))
d = str(input('Что с ними нужно сделать? = '))

import random

# реестр знаний - таблица соответствий команд - заполняется в процессе обучения
# получаем реестр из текстового файла
name_file_reestr = 'reestr_ii.txt'
reestr = {}
with open(name_file_reestr) as file:
    for line in file:
        key, value = line.split('::')
        value = value.replace('\n', '')
        reestr[key] = value
file.close()


# инструменты
instruments = ['+','-','*','/'] # заполняется в процессе получения инструментов, инструментами в дальнейшем могут быть также программы, функции, скрипты

# функция соответствия инструментов действиям 1 к 1
def dsfunct (a,b,ds):
    if ds == '+':
        res = a + b
    elif ds == '-':
        res = a - b
    elif ds == '*':
        res = a * b
    elif ds == '/':
        res = a / b
    else:
        res = 'у меня пока нет такого инструмента'
    return res


# точный ответ или эксперимент с дальнейшим обучением (наполнением реестра)
if d in reestr:
    ds = reestr[d]
    res = dsfunct(a,b,ds)
    print ('Точный ответ: ' + str(res))
else:
    #res = 'я еще не умею решать, но буду делать эксперименты со своими инструментами'
    os = ''
    old_var = []
    while os != 'да': # программа делает эксперименты, пока не ответит верно
        e = len(instruments) - 1
        rand_experiment = random.randint(0, e)
        v = 1
        while rand_experiment in old_var:
            rand_experiment = random.randint(0, e)
            if v > 10: break
            v += 1
        old_var.append(rand_experiment)
        
        ds = instruments[rand_experiment]
        exp_res = dsfunct(a,b,ds)
        print ('Экспериментальный ответ:' + str(exp_res))
        os = str(input('Мой ответ правильный? = '))
    if os == 'да':
        print ('Отлично, я угадала точный ответ и запомню механизм:' + str(exp_res))
        # запись в реестр знаний
        f = open(name_file_reestr, 'a') #Открыть файл для дозаписи
        f.write('\n' + d + '::' + ds)
        f.close()
