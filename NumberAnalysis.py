#Number Analysis
#Jason Veals
#6-23=2016

import random

def main():
    numbers = [0]*10
    for i in range(10):
        numbers[i] = random.randint(1,100)

    lowNum  = lowestNumber(numbers)
    highNum = highestNumber(numbers)
    total   = sumOfNumbers(numbers)
    printOutput(numbers,lowNum,highNum,total)

#Gets the lowest number
def lowestNumber(numbers):
    lowNum = 100
    for i in range(10):
        if numbers[i] < lowNum:
            lowNum = numbers[i]
    return lowNum

#Gets the highest number
def highestNumber(numbers):
    highNum = 1
    for i in range(10):
        if numbers[i] > highNum:
                highNum = numbers[i]
    return highNum

#Gets the total of numbers
def sumOfNumbers(numbers):

    total = 0
    for i in range(10):
        total += numbers[i]
    return total

#prints the output
def printOutput(numbers,lowNum,highNum,total):

    print('[ ',end = "")
    
    for i in range(10):
        if i == 9:
            print(numbers[i],']')
        else:
            print(numbers[i],',',end = "")

    print('Highest: ',highNum)
    print('Lowest:  ',lowNum)
    print('Sum:     ',total)
    print('Average: ',(total/10))

main()
