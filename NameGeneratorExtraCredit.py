#Name Generator Extra Credit
#Jason Veals
#6-27-2016

import random

def main():
    namesInFile = open('names.txt','r')
    descriptorsInFile = open('descriptors.txt','r')
    titlesInFile = open('titles.txt','r')
    namesOutFile = open('CharacterNames.txt','w')
    
    names = loadFile(namesInFile)
    descriptors = loadFile(descriptorsInFile)
    titles = loadFile(titlesInFile)
    outPut = [" "]*10

    for i in range(10):
        outPut[i] = format(titles[random.randint(0,len(titles) - 1)] 
                    + " " + names[random.randint(0,len(names) - 1)]
                    + " " + names[random.randint(0,len(names) - 1)]
                    + " the "
                    + descriptors[random.randint(0,len(descriptors) - 1)]
                    + "\n")

    dumpFile(namesOutFile,outPut)

    namesInFile.close()
    descriptorsInFile.close()
    titlesInFile.close()
    namesOutFile.close()    
                    
def loadFile(infile):
    names = infile.readlines()
    for i in range(len(names)):
        names[i] = names[i].rstrip()
    return names

def dumpFile(outFile,outPut):
    for i in range(len(outPut)):
        outFile.write(outPut[i])        

main()
