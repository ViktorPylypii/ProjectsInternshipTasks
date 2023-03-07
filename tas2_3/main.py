# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pascal_row(n):

    row = [1]
    for i in range(1, n+1):
        next_val = row[-1] * (n-i+1) // i
        row.append(next_val)
    return row


n = 10
row = pascal_row(n)
print(f"Рядок номер {n} у трикутнику Паскаля: {row}")

