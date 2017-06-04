# Jason Veals
# Miles Per Gallon
# 5 - 28 - 2016

def main():
    yesContinue     = "y"
    doNotContinue   = "n"
    continueProgram = yesContinue

#Gives user option to perform multiple calculations without having to restart program
#Calls necessary functions to perform program
#Gets user input for miles driven and the gallons of gas used
#Process the input
#Prints the output

    while continueProgram == yesContinue:  
        milesDriven, gallonsUsed = get_input()
        milesPerGallon = process_input(milesDriven,gallonsUsed)
        print_output(milesPerGallon)
        continueProgram = ask_user_to_continue(yesContinue,doNotContinue)
    print_goodbye_message()

#Gets the user input
def get_input():
    validInput        = "good"
    invalidInput      = "bad"
    userInput         = invalidInput

    while userInput == invalidInput:
        try:
            milesDriven = float(input('Input the miles driven for your trip '))
            gallonsUsed = float(input('Input the gallons used for your trip '))
            if gallonsUsed == 0 :
                print('Invalid input try again')
            else:
                userInput = validInput
        except:
            print()
            print('Unexpected error or invalid user input')
            print('Please retry again')
            print()

    return milesDriven, gallonsUsed

#Process user input
def process_input(milesDriven,gallonsUsed):
    milesPerGallon = milesDriven / gallonsUsed
    return milesPerGallon

#Prints the converted output
def print_output(milesPerGallon):

    topAndBottomBorder  = "############################################"
    titleHeader         = "               Miles Per Gallon             "
    print ()
    print (topAndBottomBorder)
    print ()
    print (titleHeader)
    print ()
    print (topAndBottomBorder)
    print ()
    print ('   The miles per gallon is', milesPerGallon, 'MPG')
    print ()
    print (topAndBottomBorder)
    print ()
    print ()
    print (topAndBottomBorder)
    print ()

#Prompts user to continue program or perform another conversion    
def ask_user_to_continue(yesContinue,doNotContinue):
    validInput        = "good"
    invalidInput      = "bad"
    userInput         = invalidInput

    while userInput == invalidInput:
        print ('Would you like to perform another calculation?')
        print ()
        userContinueOption = input('Enter y for yes or n for no :')
        print ()
        if userContinueOption == yesContinue or userContinueOption == doNotContinue:
            userInput = validInput
        else:
            print('You entered an invalid or unexpected response')
            print('Please enter a valid response')
            print()
            
    return userContinueOption

#prints goodbye message
def print_goodbye_message():
    print('Good bye. Have a nice day')
    
main()
