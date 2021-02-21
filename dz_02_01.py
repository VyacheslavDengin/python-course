# Домашние задание. Урок №2 задание №1-2

import random                                                                   # Импортируем модуль random

deposit = 10000                                                                 # Депозит игрока
event_log = []                                                                  # Журнал событий
log_counter = 0                                                                 # Cчётчик журнала событий
count = 0                                                                       # Счётчик вывода журнала событий

name = input('Введи своё имя: ')                                                # Приветствие игрока
print(name, ', рады тебя видеть в нашем виртуальном казино!')

print('Тебе предоставляется депозит в ', deposit,                               # Правила игры
      'единиц, \nтвоя задача угадать число в промежутке от 2 до 12, которое загадала программа.')

print('\nБросок кубиков...')                                                    # Бросок кубиков
dice_roll = random.randint(2, 12)                                               # Генерация рандомного числа
event_log.append(dice_roll)                                                     # Запись в журнал броска кубиков
player_number = int(input(name + ', введи число: '))                            # Ввод числа игрока
event_log.append(player_number)                                                 # Запись в журнал ввода игрока
log_counter += 1                                                                # Увеличиваем счечик журнала на один

while deposit > 0:                                                              # Цикл игры
   if player_number == dice_roll:                                               # Проверяем условие
       print('\nОтлично! Ты угадал!!!')
       deposit += 1000                                                          # Если угадал число, увеличиваем депозит
       event_log.append(deposit)                                                # Запись в журнал депозита
       print('Число программы ', dice_roll, '\nТвоё число ', player_number,     # Вывод результата игры
             'Твой депозит = ', deposit)
       print('\nБросок кубиков...')
       dice_roll = random.randint(2, 12)                                        # Генерация рандомного числа
       player_number = int(input(name + ', введи число: '))                     # Ввод числа игрока
       event_log.append(dice_roll)                                              # Запись в журнал броска кубиков
       event_log.append(player_number)                                          # Запись в журнал ввода игрока
       log_counter += 1                                                         # Увеличиваем счечик журнала на один
   else:
       print('\nНе угадал :(')
       deposit -= 1000                                                          # Если не угадал число, уменьшаем депозит
       event_log.append(deposit)                                                # Запись в журнал депозита
       print('Число программы ', dice_roll, '\nТвоё число ', player_number,     # Вывод результата игры
             'Твой депозит = ', deposit)
       if deposit > 0:                                                          # Если депозит больше нуля продолжаем играть
          print('\nБросок кубиков...')
          dice_roll = random.randint(2, 12)                                     # Генерация рандомного числа
          player_number = int(input(name + ', введи число: '))                  # Ввод числа игрока
          event_log.append(dice_roll)                                           # Запись в журнал броска кубиков
          event_log.append(player_number)                                       # Запись в журнал ввода игрока
          log_counter += 1                                                      # Вывод результата игры

print('\nТы все проиграл...')
print('\nЖурнал событий:')

for i in range(log_counter):                                                    # Вывод журнала событий
    print('игра загадала:', event_log[count], 'твоя попытка:', event_log[count + 1], 'на счету:', event_log[count + 2])
    count += 3
