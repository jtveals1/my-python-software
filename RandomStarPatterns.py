#Random Star Patterns
#Jason Veals
#6-10-2016

def main():
    print("Enter 5 integers between 1 and 15")
    print()
    
    for num in range(5):
        userInput = int(input("How many :"))
        for num in range(userInput):
            print("*", end = "")
        print()

main()    
