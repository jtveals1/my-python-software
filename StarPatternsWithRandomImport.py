#Star Patterns with Random Import
#Jason Veals
#6-10-2016

import random

def main():
    
    for num in range(50):
        randomNum = random.randint(1,50)
        for num in range(randomNum):
            print("*", end = "")
        print()

main()    
