#!/usr/bin/env python3

import sys
#from collections import Counter

#print(Counter(sys.argv[1]))

length=0

for i in sys.argv[1]:
    if i.islower() or i.isupper():
        length+=1

#length=len(sys.argv[1])
if length==3:
    print('Длина слова', length, 'Триграмма', sys.argv[1])

sys.exit(length)
