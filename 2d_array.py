# КОНСТАНТЫ
TO_WIN = 77
PLUS_MOVE = 1
MULT_MOVE = 2
START_FIRST = 7
# создаем поле
win = [] * TO_WIN
for i in range(TO_WIN):
    win.append([0] * TO_WIN)
for i in range(len(win)):
    for j in range(len(win)):
        if i == 0 or j == 0:
            win[i][j] = -1 # Устанавливаем соответствие индекса количеству камней в куче

for i in range(1, len(win)):
    for j in range(1, len(win)):
        # если из положения (i,j) удвоение какой-либо кучи ведет к победе, ставим единицу
        if i * 2 + j >= TO_WIN and win[i][j] == 0: # заполняем очевидные выигрышные позиции
            win[i][j] = 1
        if i + j * 2 >= TO_WIN and win[i][j] == 0: # заполняем очевидные выигрышные позиции
            win[i][j] = 1

#print(win)
for index in range(1):
    for i in range(len(win) - 1, 0, -1):    # заполнаем остальные
        for j in range(len(win) - 1, 0, -1):
            # Если все ходы ведут в нечетные клетки, ход проигрышный - заполняем его четным числом
            # Количество ходов выбираем максимальное, чтобы затянуть игру
            if win[i][j] == 0 and (win[i+PLUS_MOVE][j] % 2 == 1 and win[i*MULT_MOVE][j] % 2 == 1 and win[i][j+PLUS_MOVE] % 2 == 1 and win[i][j*MULT_MOVE] % 2 == 1):
                win[i][j] = max(win[i+PLUS_MOVE][j], win[i*MULT_MOVE][j], win[i][j+PLUS_MOVE], win[i][j*MULT_MOVE]) + 1
            # Если есть ход, который ведет в четную клетку, заполняем его нечетным числом
            # Количество ходов выбираем минимальное, чтобы быстрее закончить игру
            elif win[i][j] == 0 and (win[i+PLUS_MOVE][j] % 2 == 0 or win[i*MULT_MOVE][j] % 2 == 0 or win[i][j+PLUS_MOVE] % 2 == 0 or win[i][j*MULT_MOVE] % 2 == 0) and (win[i+PLUS_MOVE][j] * win[i*MULT_MOVE][j] * win[i][j+PLUS_MOVE] * win[i][j*MULT_MOVE]) != 0:
                min_steps = 10000
                if win[i+PLUS_MOVE][j] < min_steps and win[i+PLUS_MOVE][j] % 2 == 0:
                    min_steps = win[i+PLUS_MOVE][j]
                if win[i*MULT_MOVE][j] < min_steps and win[i*MULT_MOVE][j] % 2 == 0:
                    min_steps = win[i*MULT_MOVE][j]
                if win[i][j+PLUS_MOVE] < min_steps and win[i][j+PLUS_MOVE] % 2 == 0:
                    min_steps = win[i][j+PLUS_MOVE]
                if win[i][j*MULT_MOVE] < min_steps and win[i][j*MULT_MOVE] % 2 == 0:
                    min_steps = win[i][j*MULT_MOVE]
                win[i][j] = min_steps + 1

# Выводим итоговый массив
# print('____', end='')
# for i in range(len(win)):
#     print(i, ' ', end='')
# print('')
# for i in range(len(win)):
#    print(i, win[i])

# вывод только 7 камней в первой куче
print(win[START_FIRST])
