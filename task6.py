# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

a = int(input('Введите шестизначный номер билета: '))
left = 0
right = 0
for i in range(6):
    if i < 3:
        right += a // 10**i % 10
    else:
        left  += a // 10**i % 10
if left == right:
    print('Счастливый билет')
else:
    print('Несчастливый билет')
