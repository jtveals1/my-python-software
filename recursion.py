def main():
    num = multiply(8,4)
    print(num)
    
def multiply(x,y):
    if x == 1:
        return y
    else:
        return multiply(x-1,y + 4)

main()
