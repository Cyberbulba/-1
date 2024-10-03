while True:
    a = input('Введите первую сторону: ')
    b = input('Введите первую сторону: ')
    c = input('Введите первую сторону: ')
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        break
    else:
        print('Требуется ввести все три натуральных числа')
if not (a + b > c and a + c > b and b + c > a):
    exit('Треугольника с такими сторонами не существует')
if b >= a and b >= c:
    a, b = b, a
if c >= a and c >= b:
    a, c = c, a
if a ** 2 == b ** 2 + c ** 2:
    print('Треугольник прямоугольный')
elif a ** 2 > b ** 2 + c ** 2:
    print('Треугольник тупоугольный')
else:
    print('Треугольник остроугольный')