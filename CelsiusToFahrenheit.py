#Converts Celsius to Fahrenheit
#Jason Veals
#5-23-2016

def main():
    yesContinue     = "y"
    doNotContinue   = "n"
    continueProgram = yesContinue

#Gives user option to perform multiple calculations without having to restart program
#Calls necessary functions to perform program
#Gets user input for celsius temperature
#Process the input
#Prints the output
    
    while continueProgram == yesContinue:  
        celsiusTemp = get_input()
        fahrenheitTemp = process_input(celsiusTemp)
        print_output(fahrenheitTemp)
        continueProgram = ask_user_to_continue(yesContinue,doNotContinue)
    print_goodbye_message()

#Gets the user input
def get_input():
    validInput        = "good"
    invalidInput      = "bad"
    userInput         = invalidInput

    while userInput == invalidInput:
        try:
            celsiusTemperatureInput = float(input('Enter temperature in Celsius: '))
            userInput = validInput
        except:
            print()
            print('Unexpected error or invalid user input')
            print('Please retry again')
            print()
    return celsiusTemperatureInput

#Process user input
def process_input(celsius):
    fahrenheitDegrees = (celsius * 9/5) + 32
    return fahrenheitDegrees

#Prints the converted output
def print_output(convertedTemp):

    topAndBottomBorder  = "********************************************"
    sideBorder          = "*                                          *"
    titleHeader         = "*     Celsius Conversion to Fahrenheit     *"
    print ()
    print (topAndBottomBorder)
    print (sideBorder)
    print (titleHeader)
    print (sideBorder)
    print (topAndBottomBorder)
    print ('%% The temperature in Fahrenheit is', convertedTemp, '%%')
    print (topAndBottomBorder)
    print (sideBorder)
    print (sideBorder)
    print (topAndBottomBorder)
    print ()

#Prompts user to continue program or perform another conversion    
def ask_user_to_continue(yesContinue,doNotContinue):
    validInput        = "good"
    invalidInput      = "bad"
    userInput         = invalidInput

    while userInput == invalidInput:
        print ('Would you like to perform another conversion?')
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
