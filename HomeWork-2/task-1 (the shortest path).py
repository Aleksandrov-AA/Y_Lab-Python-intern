import itertools

postOffice = (0, 2)
griboedovStreet = (2, 5)
bakerStreet = (5, 2)
boishayaSadovayaStreet = (6, 6)
evergreenAlley = (8, 3)

def getRoute(pointX, pointY):
    result = ((pointY[0] - pointX[0]) ** 2 + (pointY[1] - pointX[1]) ** 2) ** 0.5
    return result

points = [postOffice, griboedovStreet, bakerStreet, boishayaSadovayaStreet, evergreenAlley]
array = list(itertools.permutations(points[1:]))
current = points[0]
minimum = 100

for item in array:
    result = {}
    route = 0
    item = list(item)
    item.insert(0, current)
    
    for i in range(1, len(item)):
        route = route + getRoute(item[i - 1], item[i])
        result[item[i]] = route
    
    route = route + getRoute(current, item[i])
    result[current] = route
    
    if route < minimum:
        minimum_result = result
        minimum = route

print(current, end=' ')

for a, b in minimum_result.items():
    print(f'-> {a}[{b}]', end=' ')

print('=', minimum_result[current])