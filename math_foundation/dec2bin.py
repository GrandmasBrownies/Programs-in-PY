# 2026 Joel Tann

import sys

for line in sys.stdin:
    dec = int(line)

    binary = ""
    
    if (dec == 0):
        binary = "0"

    while (dec > 0):
        binary = f'{dec % 2}' + binary
        dec = int(dec / 2)
    
    print(binary)