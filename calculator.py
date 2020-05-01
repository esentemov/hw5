while True:
    calc = input(
        "Какое действие вы хотите выполнить?"
        "Введите:\nдля сложения '+' \nдля вычитания '-'\nдля умножения '*'\nдля деления '/'"
        "если хотите закончить вычисление 'stop'\n"
    )
    if calc == 'stop':
        break
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))


    def res1(result):
        if result / round(result) != 1:
            print('{:.3f}'.format(result))


    # если итоговое значение не целочисленное, то выводить 3 знака после запятой

    def res2(result):
        if result / round(result) == 1:
            print(int(result))


    # если итоговое значение получится целочисленным, то оно будет выводится не как 5.0, а как 5

    if calc == '+':
        result = a + b
        res1(result)
        res2(result)

    elif calc == '-':
        result = a - b
        res1(result)
        res2(result)

    elif calc == "*":
        result = a * b
        if result != 0:
            res1(result)
            res2(result)
        elif result == 0:
            print(int(a * b))

    elif calc == '/':
        if b != 0:
            result = a / b
            res1(result)
            res2(result)
        elif b == 0:
            print("Ошибка, на 0 делить нельзя")