m = int(input('Enter m: '))
n = int(input('Enter n: '))

if m < n:
    m, n = n, m

while True:
    r = m % n
    if r == 0:
        print(f'GCD of ({m}, {n}) is {n}')
        exit(0)

    m = n
    n = r

