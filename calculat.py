def calculation():
    calc = input ("'+', '-', '/', '*', \nКакую операцию будем выполнять?:")
    a = float(input('Введите первое число:'))
    b= float(input('Введите второе число:'))

    if calc == '+':
        c = a + b
        print('\nРезультат сложения:' + str(c))

    elif calc == '/':
        try:
            c = a / b
            print('\nРезультат деления:' + str(c))
        except ZeroDivisionError:
            print('На ноль делить нельзя')

    elif calc == '*':   
        c = a * b
        print('\nРезультат умножения:' + str(c))

    elif calc == '-':
        c = a - b
        print('\nРезультат вычитания:' + str(c))

    else:
        print ('\nНеизвестный символ.')
    input()

print(calculation())