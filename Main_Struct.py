from tenacity import *
from ast import literal_eval
#def
import sys
import time

def bins(n):
    b_num = list(n)
    value = 0

    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    print(f"The Decimal Form is: {value}")
    time.sleep(3)

def line():
    for i in range(50):
        print("-",end='')
@retry(stop=stop_after_attempt(2))
def starting():
    temp = input("\nType 'h' or 'd' or 'b':")
    time.sleep(0.1)
    print(f"\nSo You type '{temp}'")
    for i in temp:
        if i == 'h':
            try:
                time.sleep(0.1)
                hexa = input("\nIf You Wish Don't Run The Program Just Type! 'q'\nPlease Type The Hex Input To Convert Into Deciaml And Binary:")
                if hexa == 'q':
                    print("Exiting HexaDecimal Input!")
                    exit()
                else:
                    time.sleep(0.1)
                    print(f"In The Decimal Form: {literal_eval(hexa)}")
                    print(f"In The Binary Form: {(bin(int(hexa,16)))}")
                    time.sleep(3)
            except ValueError:
                print("Only Hex Numbers!")
                print("Hex Numbers Look Like 0x1,0x3, etc.")
                time.sleep(5)
                line()
        elif i == 'd':
            line()
            time.sleep(0.1)
            print("\nEntering Decimal Mode")
            time.sleep(0.1)
            line()
            time.sleep(0.1)
            deci = input("\nIf You Wish Don't Run The Program Just Type! 'q'\nPlease Type The Decimal Input To Convert Into Hex And Binary:")
            try:
                time.sleep(0.1)
                if deci == 'q':
                    sys.exit("Exiting Binary Form")
                else:
                    print(f"In The Hexadecimal Form: {(int(deci))}")
                    print(f"In The Binary Form: {(bin(int(deci,16)))}")
                time.sleep(5)
            except ValueError:
                print("Only Decimal And Integers Accepted!")
                print("Type Some Simple Numbers like 1,2,3, etc.")
                line()
                time.sleep(3)
        elif i == 'b':
            line()
            time.sleep(0.1)
            print("\nEntering Binary Form")

            time.sleep(0.1)
            bina = input("\nIf You Wish Don't Run The Program Just Type! 'q'\nType The Binary Input To Convert In Hexadecimal And Decimal Form:")

            try:
                time.sleep(0.1)
                if bina == 'q':
                    sys.exit("Exiting Binary Form")
                else:
                    print(f"\nIn The HexaDecimal Form: {(hex(int(bina,2)))}")
                    print(bins(bina))
            except ValueError:
                print("\nOnly Binary Numbers:")
        elif temp == "q":
            line()
            print("\nPress The Close Button Or This Program Runs Until You Give 3 Wrong Input")
        else:
            print("\nPlease Only Select From 'h' or 'd' or 'b' ")
            time.sleep(3)

"""
for i in range(0,100):
    while True:
        try:
            # do stuff
        except SomeSpecificException:
            continue
        break"""

if __name__ == '__main__':
    print("Welcome To Decimal To Hex Or Binary Converter")
    print("\nPlease Type The 'h' for hex input")
    line()
    print("\nPlease Type The 'd' for decimal input")
    line()
    print("\nPlease Type The 'b' for binary input")
    line()
    time.sleep(0.1)
    for i in range(0,3):
        while True:
            try:
                starting()
            except:
                continue
            break