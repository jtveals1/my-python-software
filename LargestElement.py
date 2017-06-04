#largestelement
#jason veals
#7-15-16

import random

def main():
    numbers = [0]*10
    for i in range(10):
        numbers[i] = random.randint(1,100)
    for i in range(10):
        print(numbers[i])
    highNum = getLargest(numbers,(len(numbers) - 1))
    print()
    print('high num = ',highNum)

def getLargest(numbers,counter):
    if counter == 0:
        if numbers[counter] > numbers[counter + 1]:
            return numbers[counter]
        else:
            return numbers[counter +1]
    elif numbers[counter] > numbers[counter - 1]:
        numbers[counter - 1] = numbers[counter]
        return getLargest(numbers,counter - 1)
    else:
        return getLargest(numbers,counter - 1)

main()
