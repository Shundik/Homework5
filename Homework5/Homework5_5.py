a = input('Введите число: ')


def num(a):
    while True:
        if a.isdigit():
            int(a)
            b = 'Вы ввели положительное целое число: '
            return b + a
        if '-' in a:
            if '.' in a:
                float(a)
                b = 'Вы ввели отрицательно дробное число: '
                return b + a
            else:
                b = 'Вы ввели отрицательно целое число: '
                int(a)
                return b + a
        if '.' in a:
            b = 'Вы ввели положительно дробное число: '
            float(a)
            return b + a
        else:
            b = 'Вы ввели не корректное число: '
            return b + a


print(num(a))
