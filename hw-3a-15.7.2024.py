num = int(input("Enter a positive number greater than 0: "));

# הדפסת החלק הראשון של הצורה
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# הדפסת החלק השני של הצורה
for i in range(num - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
