l = [5, 4, 1, 2, 3]
for i in range(1, len(l)):
    curr = l[i]
    prev = i - 1

    while prev >= 0 and l[prev] > curr:
        l[prev + 1] = l[prev]

        prev = prev - 1

    l[prev + 1] = curr

print(l)
