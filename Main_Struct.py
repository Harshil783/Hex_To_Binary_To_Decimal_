import time 
def IsNumericBase(s, base):
 try:
  int(s, base)
  return True
 except ValueError:
  return False
def isDeci(s):
    return IsNumericBase(s, 10)
# Returns True if <s> is binary number string
def IsBinaryString(s):
 return IsNumericBase(s, 2)

# Returns True if <s> is octal number string
def IsOctalString(s):
 return IsNumericBase(s, 8)

# Returns True if <s> is hexadecimal number string
def IsHexadecimalString(s):
 return IsNumericBase(s, 16)

#Main Def Starting
def maincheck(temp):
    a = isDeci(temp)
    if a == False:
        b = IsBinaryString(temp)
        if b == False:
            oc = IsOctalString(temp)
            if oc == False:
                hexa = IsHexadecimalString(temp)
                if hexa == False:
                    print("Only Hex,Numbers,Binary And Octal Are Supported")
                    time.sleep(4)
                else:
                    todeci = int(temp,16)
                    print("The " + str(temp) +" In Decimal Number Is = ",int(temp, 16))
                    print("The " + str(temp) +" In Binary Number Is = ",bin(todeci).replace("0b",""))
                    print("The " + str(temp) + " In Octal Number Is = ",oct(todeci))
                    time.sleep(4)
            else:
                todeci = int(temp,8)
                print("The " + str(temp) +" In Decimal Number Is = ",int(temp,8))
                print("The " + str(temp) +" In Binary Number Is = ",bin(todeci).replace("0b",""))
                print("The " + str(temp) + " In Hex Number Is = ",hex(todeci))
                time.sleep(4)
        else:
            todeci = int(temp,2)
            print("The " + str(temp) +" In Decimal Number Is = ",int(temp, 16))
            print("The " + str(temp) +" In Hex Number Is = ",hex(todeci))
            print("The " + str(temp) + " In Octal Number Is = ",oct(todeci))
            time.sleep(4)
    else:
        todeci = int(temp,10)
        print("The " + str(temp) +" In Hex Number Is = ",hex(todeci))
        print("The " + str(temp) +" In Binary Number Is = ",bin(todeci).replace("0b",""))
        print("The " + str(temp) + " In Octal Number Is = ",oct(todeci))
        time.sleep(4)
#Main Def Ending 

if __name__ == "__main__":
    print("\t\tWelcome To Hex_To_Decimal_Binary_Octal\n")
    #for i in range(1,6):
    temp = input("Please Type The Number: ")
    for i in temp:
        if IsOctalString == True:
            if i == '0o':
                temp.replace("0o")
            else:
                pass
        else:
            pass
    maincheck(temp)
