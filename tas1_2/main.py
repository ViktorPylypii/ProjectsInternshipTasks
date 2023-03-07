# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

index = int(input("Введіть індекс бажаного числа Фібоначчі: "))
fibonacci_number = fibonacci(index)
print(f"Число Фібоначчі з індексом {index} дорівнює {fibonacci_number}")
