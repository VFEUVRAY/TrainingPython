import sys
import re

if len(sys.argv) < 3:
    print ("not enough arguments")
    exit()
if not sys.argv[2].isdigit() or sys.argv[1].isdigit():
    print ("ERROR")
    exit()
wordlen = int(sys.argv[2])
#re.split('\s', sys.argv[1])
delims = ',;:!?.'
new_string = sys.argv[1]
for c in delims:
    new_string = new_string.replace(c, ' ')
reg_split = sys.argv[1]
list_split = [word for word in re.split(' |,|\\.', reg_split) if len(word) > 0]
print (list_split)
l = [word for word in new_string.split() if len(word) >= wordlen]
print (l)