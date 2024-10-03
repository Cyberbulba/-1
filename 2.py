while True:
    num_1 = input('Введите первую переменную: ')
    num_2 = input('Введите вторую переменную: ')
    if str(abs(int(num_1))).isdigit() and str(abs(int(num_2))).isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)
        break
    else:
        print('Требуется ввести оба числа')
# способ 1
'''a = num_1
num_1 = num_2
num_2 = a'''
# способ 2
'''summa = num_1 + num_2
num_1 = summa - num_1
num_2 = summa - num_2'''
# способ 3
'''proizv = num_1 * num_2
num_1 = proizv // num_1
num_2 = proizv // num_2'''
# способ 4
num_1, num_2 = num_2, num_1
print('Первая переменная: ', num_1)
print('Вторая переменная: ', num_2)