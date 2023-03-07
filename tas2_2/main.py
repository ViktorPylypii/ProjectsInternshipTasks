# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re


def count_word_occurrences(word, mode, file_path):

    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found")
        return

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    words = text.split()

    # підрахунок кількості згадувань слова
    count = 0
    for w in words:
        if mode == 1 and word in w:
            count += 1
        elif mode == 2 and word == w:
            count += 1

    # виведення результату
    print("Number of word occurrences:", count)


count_word_occurrences("зуб", 1, 'file.txt')
