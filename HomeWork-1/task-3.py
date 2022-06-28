def zeros(n):
    if n == 0:
        return 0
    result = 0
    while n > 0:
        n //= 5
        result += n    
    return result
    

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

