#Jason Veals
#7-9-16
#Fibonacci Series
#This program uses recursion to calculate the Fibonacci Sequence

def main():

    num = int(input('Input a number for the Fibonacci Series: '))
    print()
    fibNum = F(num)
    print('F(',num,') = ',fibNum)
    
def F(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return F(num-1) + F(num-2)

main()
