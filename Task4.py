# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).


def EnteredQuarter():
    while True:
        try:
            quarter = int(input('Enter number of the quarter from 1 to 4: '))
            if quarter >= 1 and quarter <= 4:
                break
        except:
            print('Quarter must be int and between 1 and 4')

    return quarter

quarter = EnteredQuarter()

def DefinValue (quarter:int):
    if quarter == 1:
        print(f'{quarter} quarter: x>0 and y>0')
    elif quarter == 2:
        print(f'{quarter} quarter: x<0 and y>0')
    elif quarter == 3:
        print(f'{quarter} quarter: x<0 and y<0')
    else:
        print(f'{quarter} quarter: x>0 and y<0')

DefinValue(quarter)




