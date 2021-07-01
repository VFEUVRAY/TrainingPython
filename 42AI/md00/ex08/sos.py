import sys

morse = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-', ' ' : '/'}

if (len(sys.argv) < 2):
    print ("ERROR")
    exit()
message = sys.argv[1]
for mes in sys.argv[1:]:
    print(*[morse[letter.upper()] for letter in mes], sep=";")
print()
print(*[morse[letter.upper()] for letter in message])
print (" ".join(['%s']*len(message)) % tuple([morse[letter.upper()] for letter in message if letter.upper() in morse]))