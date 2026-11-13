m = int(input('Enter m: '))
n = int(input('Enter n: '))

if m < n:
    m, n = n, m

a_prime = 1
b = 1
a = 0
b_prime = 0
c = m
d = n

print(f'{"a'":>4}{"a":>4}{"b'":>4}{"b":>4}{"c":>4}{"d":>4}{"q":>4}{"r":>4}')

while True:
    q = c // d
    r = c % d

    if r == 0:
        print(f'\n\n{a} * {m} + {b} * {n} = {d}')
        exit(0)

    c = d
    d = r
    t = a_prime
    a_prime= a
    a = t - q * a
    t = b_prime
    b_prime = b
    b = t - q * b
    print(f'{a_prime:>4}{a:>4}{b_prime:>4}{b:>4}{c:>4}{d:>4}{q:>4}{r:>4}')

