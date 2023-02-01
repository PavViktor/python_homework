# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите кол-во долек по горизонтали '))
m = int(input('Введите кол-во долек по вертикали '))
k = int(input('Введите кол-во отломленых долек '))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')
