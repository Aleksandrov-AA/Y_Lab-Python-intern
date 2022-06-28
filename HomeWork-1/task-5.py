def count_find_num(primesL, limit):
    primes = 1
    for p in primesL:
        primes *= p
    if primes > limit:
        return []
    result = [primes]
    for i in primesL:
        p = result.copy()
        for n1 in p:
            n2 = i
            while n1 * n2 <= limit:
                result.append(n1 * n2)
                n2 *= i
        result.sort()
    return [len(result), result[-1]]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []