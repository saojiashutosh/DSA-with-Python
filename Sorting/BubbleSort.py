l = [5, 4, 3, 2, 1]

iter = len(l) - 1

while iter > 0:
    for i in range(0, iter):
        if l[i] > l[i + 1]:
            temp = l[i + 1]
            l[i + 1] = l[i]
            l[i] = temp

    iter = iter - 1

print(l)
