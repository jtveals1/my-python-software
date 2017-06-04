class CommonTasks():

    def getInput(self, inputPrompt):
        self.userInput = inputPrompt
        return float(input(self.userInput))
        
    def printOutPut(self, outPutMessage, outPutValue, outMessage):
        print(outPutMessage, outPutValue, outMessage)

    def ask_user_to_continue(self):
        self.yesContinue       = "y"
        self.doNotContinue     = "n"
        self.validInput        = "good"
        self.invalidInput      = "bad"
        self.userInput         = self.invalidInput

        while self.userInput == self.invalidInput:
            print ('Would you like to perform another calculation?')
            print ()
            self.userContinueOption = input('Enter y for yes or n for no :')
            print ()
            if self.userContinueOption == self.yesContinue or self.userContinueOption == self.doNotContinue:
               self.userInput = self.validInput
            else:
                print('You entered an invalid or unexpected response')
                print('Please enter a valid response')
                print()
        return self.userContinueOption
