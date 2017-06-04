#BrickWall program - Prints a regular and staggered brick wall
#The Total length of characters for the wall is 61
#Jason Veals
#5-29-2016

BRICKHORIZONTALLINE = '_'
BRICKVERTICALLINE   = '|'

def main():
    height = get_int_in_range('Enter height: ',1,10)
    width  = get_int_in_range('Enter width: ',1,20)
    print_Top_Of_Brick_Wall()
    full_Brick(width)
    #print_Regular_Wall()        
    #print_Staggered_Wall()


def get_int_in_range(prompt,low,high):
    userPrompt = prompt + ' between ' + str(low) + ' and ' + str(high) + ' '
    userInput = int(input(userPrompt))
    while userInput < low or userInput > high:
        print('You entered a number that is out of the specified range')
        userInput = int(input(userPrompt))
    return userInput
    
    
#Prints horizontal lines at the top of brick wall
#This function prints space at the beginning for aesthetic purposes then prints
#Horizontal characters to complete the top of the wall
def print_Top_Of_Brick_Wall():

    print(" ",end = "")
    for num in range(59):
        print(BRICKHORIZONTALLINE,end = "")
    print()

#Prints vertical line ,space, or horizontal line to create each brick
#Specifies each brick a length of 10 character spaces
#Uses the modulus operator to print when the counter is a multiple of ten
def print_Brick_Row():

    for num in range(2):
        for num in range(61):     
            if num % 10 == 0 :
                print(BRICKVERTICALLINE,end = "")
            else:
                print(' ',end = "")
        print()
    
    #Prints bottom of brick row
    for num in range(61):
        if num % 10 == 0 :
            print(BRICKVERTICALLINE,end = "")
        else:
            print(BRICKHORIZONTALLINE,end = "")
    print()

#Prints staggered row
#The first and last bricks are 5 character lengths
#The other bricks on the row are 10 character lengths
def print_Staggered_Brick_Row():

    for num in range(2):
        for num in range(61):
            if num == 0:
                print(BRICKVERTICALLINE, end = "") 
            elif num == 5:
                print(BRICKVERTICALLINE, end = "")
            elif num == 15:
                print(BRICKVERTICALLINE, end = "")
            elif num == 25:
                print(BRICKVERTICALLINE, end = "")
            elif num == 35:
                print(BRICKVERTICALLINE, end = "")
            elif num == 45:
                print(BRICKVERTICALLINE, end = "")
            elif num == 55:
                print(BRICKVERTICALLINE, end = "")
            elif num == 60:
                print(BRICKVERTICALLINE, end = "")
            else:
                print(' ', end = "")
        print()
        
#Prints bottom of Staggered brick row        
    for num in range(61):
        if num == 0:
            print(BRICKVERTICALLINE, end = "") 
        elif num == 5:
            print(BRICKVERTICALLINE, end = "")
        elif num == 15:
            print(BRICKVERTICALLINE, end = "")
        elif num == 25:
            print(BRICKVERTICALLINE, end = "")
        elif num == 35:
            print(BRICKVERTICALLINE, end = "")
        elif num == 45:
            print(BRICKVERTICALLINE, end = "")
        elif num == 55:
            print(BRICKVERTICALLINE, end = "")
        elif num == 60:
            print(BRICKVERTICALLINE, end = "")
        else:
            print(BRICKHORIZONTALLINE, end = "")
    print()
    
#Prints staggered wall
#Two brick rows equals one staggered section
def print_Staggered_Wall():

    numOfStaggeredSections = 2

    print_Top_Of_Brick_Wall()  
    for num in range(numOfStaggeredSections):
        print_Staggered_Brick_Row()
        print_Brick_Row()

#Prints regular wall    
def print_Regular_Wall():

    numOfBrickRows= 4

    print_Top_Of_Brick_Wall()
    for num in range(numOfBrickRows):    
        print_Brick_Row()

main()




