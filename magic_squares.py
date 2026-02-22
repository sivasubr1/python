import numpy as np

def duplicates(number):
    digits = [int(digit) for digit in str(number)]

    return len(digits) != len(set(digits))


def convert_to_square(number):
    digits = [int(digit) for digit in str(number)]

    square = np.array(digits).reshape(-1, 3)

    row_sums = np.sum(square, axis=1)

    magic_sum = -1

    if len(set(row_sums)) == 1:
        magic_sum = row_sums[0]

    col_sums = np.sum(square, axis=0)

    if (len(set(col_sums)) == 1 and
        col_sums[0]                 == magic_sum and
        np.trace(square)            == magic_sum and
        np.trace(np.fliplr(square)) == magic_sum):
        print(square)


for i in range(111111111, 1000000000):
    if duplicates(i):
        continue

    if '0' in str(i):
        continue

    convert_to_square(i)
