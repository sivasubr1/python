from itertools import permutations, filterfalse

K = 5

pairs_list = []

def langford_pairs(l):
    for i in range(1, K):
        first = l.index(i)
        second = l.index(i, first + 1)
        if second - first - 1 != i:
            return False

    return True

for i in range(1, K):
    pairs_list.append(i)
    pairs_list.append(i)

p = list(permutations(pairs_list))

for l in p:
    if langford_pairs(l):
        print(l)
