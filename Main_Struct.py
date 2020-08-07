from ast import literal_eval
import time
print("Welcome To Decimal To Hex Or Binary Converter")
def line():
    for i in range(50):
        print("-",end='')
print("\nPlease Type The 'h' for hex input")
line()
print("\nPlease Type The 'd' for decimal input")
line()
print("\nPlease Type The 'b' for binary input")
line()
temp = input("\nType 'h' or 'd' or 'b':")
line()
time.sleep(1)
print(f"\nSo You type '{temp}'")
time.sleep(1)

for i in temp:
    if i == 'h':
        try:
            time.sleep(1)
            hexa = input("\nPlease Type The Hex Input To Convert Into Deciaml And Binary:")
            time.sleep(1)
            print(f"In The Decimal Form: %s" %(literal_eval(hexa)))
            print(f"In The Binary Form: %s" %(bin(int(hexa,16))))
            time.sleep(5)
        except ValueError:
            print("Only Hex Numbers!")
            print("Hex Numbers Look Like 0x1,0x3, etc.")
            time.sleep(5)
            line()
    elif i == 'd':
        line()
        time.sleep(1)
        print("\nEntering Decimal Mode")
        time.sleep(1)
        line()
        time.sleep(1)
        deci = input("\nPlease Type The Decimal Input To Convert Into Hex And Binary:")
        try:
            time.sleep(1)
            print(f"In The Hexadecimal Form: %s" %(int(deci)))
            print(f"In The Binary Form: %s" %(bin(int(deci,16))))
            time.sleep(5)
        except ValueError:
            print("Only Decimal And Integers Accepted!")
            print("Type Some Simple Numbers like 1,2,3, etc.")
            line()
            time.sleep(5)
    elif i == 'b':
        line()
        time.sleep(1)
        print("\nEntering Binary Form")
        line()
        time.sleep(1)
        bina = input("\nType The Binary Input To Convert In Hexadecimal And Decimal Form:")
        line()
        try:
            time.sleep(1)
            print("\nIn The HexaDecimal Form: %s" %(hex(int(bina,2))))

        except ValueError:
            print("\nOnly Binary Numbers:")
    else:
        print("Please Only Select From 'h' or 'd' or 'b' ")
        time.sleep(5)