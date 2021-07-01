import sys

for arg in sys.argv[1:]:
    for i in range(len(arg[::-1])):
        if arg[::-1][i].islower():
            print(arg[::-1][i].upper(), end='')
        else:
            print(arg[::-1][i].lower(), end='')
    print()

for arg in sys.argv[1:]:
    print (arg[::-1].swapcase())
