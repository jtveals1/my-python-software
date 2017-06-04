import random

def main():
    
    userTotal = userPlay()
    compTotal = computerPlay()
    compareTotal(userTotal,compTotal)
    
def userPlay():
    card1,card2 = generateInitialCards()
    hitme = False
    total = card1 + card2
    print('The initial value of your two cards are ',total)
    getAnotherCard = input('Would you like a hit. enter y or n ')

    if getAnotherCard == 'y':
        hitme = True
        
    while hitme:
        nextCard = getAnotherHit()
        if total > 10 and nextCard == 11:
            nextCard = 1
        total = total + nextCard
        print('Your card value is ',nextCard)
        printTotal(total)
        if total > 21:
            print('You crapped out')
            print('The computer wins')
            hitme = False
        else:
            getAnotherCard = input('Would you like another hit. enter y or n ')
            if getAnotherCard == 'y':
                hitme = True
            else:
                hitme = False
    return total

def compareTotal(userTotal,compTotal):
    if userTotal <= 21:
        if compTotal > 21:
            print('The computer crapped out.')
            print('You win')
        elif userTotal == 21 and compTotal == 21:
            print('It is a tie')
        elif userTotal == 21:
            print('You hit blackjack. You win')
        elif compTotal == 21:
            print('The computer hit blackjack. The computer wins')
        else:
            userdif = 21 - userTotal
            compdif = 21 - compTotal
            if userdif < compdif:
                print('You win')
            elif compdif < userdif:
                print('The computer wins')
            elif userdif == compdif:
                print("It's a tie")
                
def printCompTotal(total):
    print("The computer's total is ",total)
    
def computerPlay():
    compCard1,compCard2 = generateInitialCards()
    total = compCard1 + compCard2
    print("The initial value of the computer's cards is ",total)
    compContinue = True
    if total >= 21 or total > 18:
        compContinue = False
    while compContinue:
        nextCard = getAnotherHit()
        if total > 10 and nextCard == 11:
            nextCard = 1
        total = total + nextCard
        if total >= 21 or total > 18:
            compContinue = False
    printCompTotal(total)
    return total
            
def printTotal(total):
    print('Your total is ',total)
    
def generateInitialCards():
    card1 = random.randint(2,11)
    card2 = random.randint(2,11)

    return card1,card2

def getAnotherHit():
    card = random.randint(2,11)
    return card
main()
