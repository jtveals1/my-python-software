def main():
    
    for i in range(7):
        for j in range(7):
            if (i == 0) and (j == 4):
                print("*",end = "")
            elif(i == 1) and (j == 3):
                print("***",end = "")
            elif(i == 2) and (j == 2):
                print("*****",end = "")
            elif(i == 3) and (j == 1):
                print("*******",end = "")
            elif(i == 4) and (j == 2):
                print("*****",end = "")
            elif(i == 5) and (j == 3):
                print("***",end = "")
            elif(i == 6) and (j == 4):
                print("*",end = "")
            else:
                print(" ",end = "")
        print()
main()
