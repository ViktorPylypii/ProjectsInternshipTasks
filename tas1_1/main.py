import os

# введення шляху до вхідного файлу
input_file_path = input("Введіть шлях до вхідного файлу: ")

# перевірка чи існує файл за вказаним шляхом
if not os.path.exists(input_file_path):
    print("Файл не існує")
    exit()

# введення шляху до вихідного файлу
output_file_path = input("Введіть шлях до вихідного файлу: ")

# відкриття вхідного файлу у режимі читання та читання даних
with open(input_file_path, "r") as input_file:
    data = input_file.read()

# обернення тексту
reversed_data = data[::-1]

# запис даних у вихідний файл
with open(output_file_path, "w") as output_file:
    output_file.write(reversed_data)

print("Дані успішно записані у зворотньому порядку у файл за шляхом", output_file_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
