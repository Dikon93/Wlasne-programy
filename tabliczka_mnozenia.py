size = int(input("Podaj wielkość: "))


def sfill(number):
    while len(number) < 3:
        number = " " + number
    return number


for a in range(1, size + 1):
    for b in range(1, size + 1):
        print(sfill(str(a*b)), end=" ")
    print()
