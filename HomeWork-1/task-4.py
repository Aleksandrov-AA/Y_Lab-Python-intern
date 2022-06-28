from itertools import combinations

def bananas(s) -> set:
    result = set()
    word = 'banana'
    numbCount = len(s) - len(word)
    pool = combinations(range(len(s)), numbCount)
    for i in pool:
        t = list(s)
        for a in i:
            t[a] = '-'
        updateStr = ''.join(t)
        if updateStr.replace('-', '') == word:
            result.add(updateStr)
    return result
    

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
