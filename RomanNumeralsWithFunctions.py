#Roman Numerals
#Jason Veals
#6-13-2016

def main():
    inputNum = getInteger()
    printRomanNumeral(inputNum)

def getInteger():
    inputNum = int(input('Input a number from 1 to 10: '))
    while inputNum < 1 or inputNum > 10:
        print("num in range")
        print('You entered invalid input')
        inputNum = int(input('Input a number from 1 to 10: '))
    return inputNum

def printRomanNumeral(inputNum):    

    if inputNum == 1:
        print('The Roman Numeral Version is: I')
        
    elif inputNum == 2:
        print('The Roman Numeral Version is: II')

    elif inputNum == 3:
        print('The Roman Numeral Version is: III')

    elif inputNum == 4:
        print('The Roman Numeral Version is: IV')

    elif inputNum == 5:
        print('The Roman Numeral Version is: V')

    elif inputNum == 6:
        print('The Roman Numeral Version is: VI')

    elif inputNum == 7:
        print('The Roman Numeral Version is: VII')

    elif inputNum == 8:
        print('The Roman Numeral Version is: VIII')

    elif inputNum == 9:
        print('The Roman Numeral Version is: IX')

    elif inputNum == 10:
        print('The Roman Numeral Version is: X')

main()
