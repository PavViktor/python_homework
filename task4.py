# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input('Введите кол-во сделаных журавликов: '))
kate = s / 3 * 2
pete = kate / 2 / 2
serj = pete
print('Катя сделала', kate, 'журавликов')
print('Петя сделал', pete, 'журавликов')
print('Сережа сделал', serj, 'журавликов')