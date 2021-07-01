import sys

if (len(sys.argv) < 2 or len(sys.argv) > 2 or  not sys.argv[1].isdigit()):
    print("ERROR")
    exit()
num = int(sys.argv[1])
if (not num):
    print("Zero")
elif (num % 2):
    print("Odd")
else:
    print("Even")