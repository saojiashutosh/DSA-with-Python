l = [5, 4, 3, 2, 1]

for i in range(0, len(l)):
    min = i
    for j in range(i + 1, len(l)):
        if l[min] > l[j]:
            min = j
    temp = l[i]
    l[i] = l[min]
    l[min] = temp

print(l)
