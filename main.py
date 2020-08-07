import time
from Main_Struct import bina
def bins():
    b_num = list(bina)
    value = 0

    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    print("The Decimal Form is: %s" %(value))
    time.sleep(5)
bins()