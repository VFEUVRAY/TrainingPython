import sys

def operations(a, b, *args):
    """
Usage: python operations.py <number1> <number2>
Example:
    python operations.y 10 3
    """
    
    print("Sum:        ", a+b)
    print("Difference: ", a-b)
    print("Product:    ", a*b)
    print("Quotient:   ", a/b if b else "ERROR (div by zero)")
    print("Remainder:  ", a%b if b else "ERROR (modulo by zero)")

if (len(sys.argv) < 2):
    print(operations.__doc__)
    exit()
if (len(sys.argv) > 3):
    print("Too many arguments\n", operations.__doc__)
    exit()
if (not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
    print ("Input error: only numbers\n", operations.__doc__)
    exit()
operations(int(sys.argv[1]), int(sys.argv[2]))
