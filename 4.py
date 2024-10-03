while True:
    x = input('Введите координату x: ')
    y = input('Введите координату y: ')
    z = input('Введите координату z: ')
    if str(abs(int(x))).isdigit() and str(abs(int(y))).isdigit() and str(abs(int(z))).isdigit():
        x = int(x)
        y = int(y)
        z = int(z)
        break
    else:
        print('Требуется ввести все три числа')
print('Длина вектора:', (x ** 2 + y ** 2 + z ** 2) ** 0.5)
