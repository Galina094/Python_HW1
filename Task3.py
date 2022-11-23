# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def InputPoint(string):
    while True:
        try:
            a = int(input(string))
            if a!=0:
                break
            else: print('Error. Entered point must be not null.')
        except:
            print('Error. Entered point must be int.')
    return a

x = InputPoint('Enter X: ')
y = InputPoint('Enter Y: ')

def CoordPlane(x:int, y:int):
    if x>0 and y>0:
        print('I quarter')
    elif x<0 and y>0:
        print('II quarter')
    elif x < 0 and y < 0:
        print('III quarter')
    elif x>0 and y<0:
        print('IV quarter')

CoordPlane(x,y)











