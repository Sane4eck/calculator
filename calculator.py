def calculator():
    num1 = float(number1)
    num2 = float(number2)
    if sign == '+':
        print(num1 + float(num2))
    elif sign == '-':
        print(num1 - num2)
    elif sign == '*':
        print(num1 * num2)
    elif sign == '/':
        if num2 == 0:
            print("На ноль делить нельзя!")
        else:
            print(num1 / num2)


def znak():
    global n
    global sign
    sign = str(input("Что нужно сделать? ('+','-','*','/') "))
    if sign == str('+'):
        n = 0
    elif sign == str('-'):
        n = 0
    elif sign == str('/'):
        n = 0
    elif sign == str('*'):
        n = 0
    else:
        n = 1


def start():
    pass


# while True:
#     choise = str(input("Запустить калькулятор? 1 - да, N - нет  "))
#     number1 = float(input("Введите число: "))
#     if number1 == int or float:
#         if choise == '1':
#             znak()
#             if n == 1:
#                 print("Нет такой функции! ")
#                 continue
#             elif n == 0:
#                 number2 = float(input("Введите еще одно число: "))
#                 if number2 == int or float:
#                     calculator()
#                 else:
#                     print("Вы ввели не число")
#                     continue
#         else:
#             break
#     else:
#         print("Вы ввели " + str(number1) + " не число")
#         continue
# print("Hi!")

while True:
    choise = str(input("Запустить калькулятор? 1 - да, N - нет  "))
    if choise == '1':
        number1 = float(input("Введите число: "))
        if number1 == int or float:
            znak()
            if n == 1:
                print("Нет такой функции! ")
                continue
            elif n == 0:
                number2 = float(input("Введите еще одно число: "))
                if number2 == int or float:
                    calculator()
                else:
                    print("Вы ввели не число")
                    continue
        else:
            break
    else:
        break
print("Goodbye!!!")
