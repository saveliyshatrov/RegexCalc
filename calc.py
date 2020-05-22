import re  # regex library

print("Калькулятор")
print("Введите 'Q' to exit\n")
print("Введите 'N' для нового примера\n")

previous = 0
run = True


def performMath():
    global run
    global previous

    if previous == 0:
        equation = input("Введите пример: ")
    else:
        equation = input(str(previous))

    if equation == 'Q':
        previous = 'quit'
        run = False
    elif equation == 'N':
        previous = 0
    else:
        if equation == '':
            print(previous)
        elif any(char.isdigit() for char in equation):
            equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
        else:
            print("Неправильный ввод")


while run:
    performMath()
