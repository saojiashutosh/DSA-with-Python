print("Enter the length of List :")
n = int(input())
l = []
print("Element of the List :")
for i in range(n):
    l.append(int(input()))

print("Enter element to Find :")
x = int(input())

for i in range(len(l)):
    if x == l[i]:
        m = i
        print(f"Element is at index : {m} ")
