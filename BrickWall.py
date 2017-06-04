#BrickWall program 
#Jason Veals
#6-26-2016

BRICKHORIZONTALLINE = '_'
BRICKVERTICALLINE   = '|'

def main():
    height = get_int_in_range('Enter height: ',1,10)
    width  = get_int_in_range('Enter width: ',1,20)
    print_Top_Of_Brick_Wall(width)
    layers = 0
    while layers < height:
        full_Brick(width)
        layers+=1
        if layers < height:
            half_Brick(width)
            layers+=1

#Get height and width of wall from user
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
def print_Top_Of_Brick_Wall(width):
    print(' ', end = "")
    for num in range((width*10) - 2):
        print(BRICKHORIZONTALLINE,end = "")
    print()

#Prints vertical line ,space, or horizontal line to create each brick
#Specifies each brick a length of 10 character spaces
def full_Brick(width):

    counter = 0
    bottomOfRow = 2
    for i in range(3):
        for j in range(width*10):     
            if counter == 0 or counter == 9:
                print(BRICKVERTICALLINE,end = "")
            #prints bottom of row
            elif i == bottomOfRow:
                print(BRICKHORIZONTALLINE,end = "")
            else:
                print(' ',end = "")
            counter += 1
            if counter == 10 :
                counter = 0
        print()
    
#Prints staggered row
def half_Brick(width):

    counter = 0
    bottomOfRow = 2
    for i in range(3):
        for j in range(width*10):
            if j == 0:
                print(BRICKVERTICALLINE, end = "") 
            elif j == 4:
                print(BRICKVERTICALLINE, end = "")
            elif j > 4 and j < (width*10) - 5:
                if counter == 0 or counter == 9 :
                    print(BRICKVERTICALLINE,end = "")
                #print bottom of row
                elif i == bottomOfRow:
                    print(BRICKHORIZONTALLINE,end = "")
                else:
                    print(' ',end = "")
                counter += 1
                if counter == 10 :
                    counter = 0
            elif j == (width*10) - 5:
                print(BRICKVERTICALLINE, end = "")
            elif j == (width*10) - 1:
                print(BRICKVERTICALLINE, end = "")
            #print bottom of row    
            elif i == bottomOfRow:
                print(BRICKHORIZONTALLINE,end = "")    
            else:
                print(' ', end = "")
        print()

main()




