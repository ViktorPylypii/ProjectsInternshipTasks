# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math

# Ввід координат точок А та В з клавіатури
x1, y1 = map(int, input("Введіть координати точки А через пробіл: ").split())
x2, y2 = map(int, input("Введіть координати точки В через пробіл: ").split())

# Обчислення косинусів кутів
cos_angle_A = x1 / math.sqrt(x1**2 + y1**2)
cos_angle_B = x2 / math.sqrt(x2**2 + y2**2)

# Порівняння косинусів та вивід результату
if cos_angle_A > cos_angle_B:
    print("Відрізок ОА утворює більший кут з віссю ОХ")
else:
    print("Відрізок ОВ утворює більший кут з віссю ОХ")
