import random

def main():
    numbers = [10,5,2,98,45,23,76,89,99,65]

    printnum(numbers)
    
    sort(numbers)
    printnum(numbers)

def sort(numbers):

    for i in range(10):
        for j in range(10):
            if numbers[i] < numbers[j]:    
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    
def printnum(numbers):
    for i in range(10):
        print(numbers[i])
    print()
main()    
            
        
