# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

X = input('Введите X:')
Y = input('Введите Y:')
Z = input('Введите Z:')

if not (X or Y or Z) == (not X or not Y or not Z):
    print(True)
else: print(False)