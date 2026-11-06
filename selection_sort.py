import numpy as np

# From the "Intro to Python for Computer Science and Data Science" Deitel book

def selection_sort(data):
    for index1 in range(len(data) - 1):
        smallest = index1

        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[smallest]:
                smallest = index2

        data[smallest], data[index1] = data[index1], data[smallest]
        print_pass(data, index1 + 1, smallest)


def main():
    data = np.array([34, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    selection_sort(data)
    print(f'\nSorted: {data}\n')


def print_pass(data, pass_number, index):
    label = f'after pass {pass_number} '
    print(label, end='')

    print('   '.join(str(d) for d in data[:index]), end='   ' if index != 0 else '')
    print(f'{data[index]}* ', end='')
    print('   '.join(str(d) for d in data[index +1:len(data)]))
    print(f'{" " * len(label)}{"-- " * pass_number}')




if __name__ == '__main__':
    main()

