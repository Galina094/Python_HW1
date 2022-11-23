# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:  - 6 -> да      - 7 -> да        - 1 -> нет


def EnteredNumOfDay():
    while True:
        day = input('Введи цифру, обозначающую день недели от 1 до 7: ')
        if not day.isnumeric():
            print('Что ты ввёл? - Неформат. ')
        elif not 1 <= int(day) <= 7:
            print('Необходимо ввести число от 1 до 7! ')
        else:
            print('Всё ОК')
            break
    return day

day = EnteredNumOfDay()

def CheckDay (day):

    if int(day) == 6 or int(day) == 7:
        print(f'{day} - отдыхаееем!!!')
    else:
        print(f'{day} - солнце еще в зените... работаем!')

CheckDay(day)






