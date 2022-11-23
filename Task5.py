# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def CheckNum(string):
    while True:
        try:
            num = int(input(string))
            break
        except:
            print('Your number not int.')
    return abs(num)

x1 = CheckNum('Enter X1: ')
y1 = CheckNum('Enter Y1: ')
x2 = CheckNum('Enter X2: ')
y2 = CheckNum('Enter Y2: ')

def Distance (x1:int,y1:int,x2:int,y2:int):
    result = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(f'sqrt(({x2} - {x1})^2+({y2} - {y1})^2) = {result:.2f}')

Distance(x1,y1,x2,y2)







