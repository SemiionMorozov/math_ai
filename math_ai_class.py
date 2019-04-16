# Экспериментальная модель машинного обучения v 2.0 (на классах) -
# на примере простых операций с числами (умный калькулятор)
# 16.04.2019 - Semion Morozov - semiion-morozov@mail.ru

import random


class MathAI:

    def file_reestr(self, file_name):
        self.reestr = {}
        with open(file_name) as file:
            for line in file:
                key, value = line.split('::')
                value = value.replace('\n', '')
                self.reestr[key] = value
        file.close()
        self.file_name = file_name


    def load_data_in_reestr(self):
        f = open(self.file_name, 'a')  # Открыть файл для дозаписи
        f.write('\n' + self.d + '::' + self.ds)
        f.close()

    def load_instruments(self, instruments):
        self.instruments = instruments

    def calc(self, a, b, ds):
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
        self.res = res

    def exact_answer(self):
        self.ds = self.reestr[self.d]
        self.calc(self.a, self.b, self.ds)
        print('Точный ответ: ' + str(self.res))

    def experiment(self):
        os = ''
        old_var = []
        while os != 'да':  # программа делает эксперименты, пока не ответит верно
            e = len(self.instruments) - 1
            rand_experiment = random.randint(0, e)
            v = 1
            while rand_experiment in old_var:
                rand_experiment = random.randint(0, e)
                if v > 10: break
                v += 1
            old_var.append(rand_experiment)

            self.ds = self.instruments[rand_experiment]

            self.calc(self.a, self.b, self.ds)
            print('Экспериментальный ответ:' + str(self.res))
            os = str(input('Мой ответ правильный? = '))
        if os == 'да':
            print('Отлично, я угадала точный ответ и запомню механизм:' + str(self.res))
            self.load_data_in_reestr() # запись в реестр знаний

    def start(self):
        self.a = int(input('Введите число a = '))
        self.b = int(input('Введите число b = '))
        self.d = str(input('Что с ними нужно сделать? = '))
        if self.d in self.reestr:
            self.exact_answer()
        else:
            self.experiment()


m = MathAI() # инициализация

m.file_reestr('reestr_ii.txt') # ссылка на файл реестра знаний
m.load_instruments(['+','-','*','/']) # Загрузка инструментов

m.start() # запуск программы