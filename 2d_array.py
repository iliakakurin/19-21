# создаем поле
win = [] * 77
for i in range(77):
    win.append([0] * 77)
for i in range(len(win)):
    for j in range(len(win)):
        if i == 0 or j == 0:
            win[i][j] = -1 # Устанавливаем соответствие индекса количеству камней в куче

for i in range(1, len(win)):
    for j in range(1, len(win)):
        # если из положения (i,j) удвоение какой-либо кучи ведет к победе, ставим единицу
        if i * 2 + j >= 77 and win[i][j] == 0: # заполняем очевидные выигрышные позиции
            win[i][j] = 1
        if i + j * 2 >= 77 and win[i][j] == 0: # заполняем очевидные выигрышные позиции
            win[i][j] = 1

#print(win)
for index in range(1):
    for i in range(len(win) - 1, 0, -1):    # заполнаем остальные
        for j in range(len(win) - 1, 0, -1):
            # Если все ходы ведут в нечетные клетки, ход проигрышный - заполняем его четным числом
            # Количество ходов выбираем максимальное, чтобы затянуть игру
            if win[i][j] == 0 and (win[i+1][j] % 2 == 1 and win[i*2][j] % 2 == 1 and win[i][j+1] % 2 == 1 and win[i][j*2] % 2 == 1):
                win[i][j] = max(win[i+1][j], win[i*2][j], win[i][j+1], win[i][j*2]) + 1
            # Если есть ход, который ведет в четную клетку, заполняем его нечетным числом
            # Количество ходов выбираем минимальное, чтобы быстрее закончить игру
            elif win[i][j] == 0 and (win[i+1][j] % 2 == 0 or win[i*2][j] % 2 == 0 or win[i][j+1] % 2 == 0 or win[i][j*2] % 2 == 0) and (win[i+1][j] * win[i*2][j] * win[i][j+1] * win[i][j*2]) != 0:
                min_steps = 10000
                if win[i+1][j] < min_steps and win[i+1][j] % 2 == 0:
                    min_steps = win[i+1][j]
                if win[i*2][j] < min_steps and win[i*2][j] % 2 == 0:
                    min_steps = win[i*2][j]
                if win[i][j+1] < min_steps and win[i][j+1] % 2 == 0:
                    min_steps = win[i][j+1]
                if win[i][j*2] < min_steps and win[i][j*2] % 2 == 0:
                    min_steps = win[i][j*2]
                win[i][j] = min_steps + 1
                
# Выводим итоговый массив
# print('____', end='')
# for i in range(len(win)):
#     print(i, ' ', end='')
# print('')
# for i in range(len(win)):
#    print(i, win[i])

# вывод только 7 камней в первой куче
# print(win[7])
