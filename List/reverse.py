l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first = 0
last = len(l) - 1

while first < last:
    temp = l[first]
    l[first] = l[last]
    l[last] = temp

    first += 1
    last -= 1

print(l)
