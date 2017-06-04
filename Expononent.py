#Exponent
#Jason Veals

def main():
    number = int(input('input number '))
    exp    = int(input('input expononent '))

    value = expononent(number,exp)
    print(value)

def expononent(number,exp):
    if exp == 0:
        print(exp)
        raisedNum = 1
        return raisedNum
    elif exp == 1:
        print(exp)
        return number
    else:
        print(exp)
        return number * expononent(number,exp - 1)
        
main()     
