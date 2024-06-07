l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    for j in range(i, len(l)):
        print(l[i : j + 1])
