# 2026 Joel Tann

import sys

for line in sys.stdin:
    dec = int(line)

    hexa = ""

    if (dec == 0):
        hexa = '0'

    while (dec > 0):
        digit = dec % 16

        if (digit == 10):
            hexa = 'a' + hexa
        elif (digit == 11):
            hexa = 'b' + hexa
        elif (digit == 12):
            hexa = 'c' + hexa
        elif (digit == 13):
            hexa = 'd' + hexa
        elif (digit == 14):
            hexa = 'e' + hexa
        elif (digit == 15):
            hexa = 'f' + hexa
        else:
            hexa = f"{digit}" + hexa

        dec = int(dec / 16)
    
    print(hexa)