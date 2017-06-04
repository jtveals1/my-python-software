#RecursiveArraySum
#jason veals
#7-15-16

import random

def main():
    numbers = [0]*10
    for i in range(10):
        numbers[i] = random.randint(1,100)
    for i in range(10):
        print(numbers[i])
    sumNum = getSum(numbers,(len(numbers) - 1))
    print()
    print('Sum = ',sumNum)

def getSum(numbers,counter):
    if counter == 0:
        return numbers[counter] 
    else:
        return numbers[counter] + getSum(numbers, counter - 1)

main()
