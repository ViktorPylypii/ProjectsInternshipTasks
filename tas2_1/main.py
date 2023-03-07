# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def merge_arrays(*arrays):
    merged = []
    for arr in arrays:
        merged += arr

    # Відфільтрувати числа, які кратні 5
    merged = list(filter(lambda x: x % 5 != 0, merged))

    # Відсортувати
    merged.sort()

    return merged



arr1 = [4, 8, 15, 16, 23, 42]
arr2 = [1, 2, 4, 8, 16, 32]
arr3 = [7, 14, 21, 28]
merged_list = sorted(list(set(arr1 + arr2 + arr3)))
result_list = list(filter(lambda x: x % 5 != 0, merged_list))
print(result_list)
