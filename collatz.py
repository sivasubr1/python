def collatz(i):
    if i == 1:
        return [1]

    if i % 2 == 0:
        return [i // 2] + collatz(i // 2)

    return [i * 3 + 1] + collatz(i * 3 + 1)


for i in range(1, 11):
    print(i, [i] + collatz(i))
