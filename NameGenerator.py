#Name Generator
#Jason Veals
#6-27-2016

import random

def main():
    namesInFile = open('names.txt','r')
    descriptorsInFile = open('descriptors.txt','r')
    titlesInFile = open('titles.txt','r')
    names = loadFile(namesInFile)
    descriptors = loadFile(descriptorsInFile)
    titles = loadFile(titlesInFile)

    output = format(titles[random.randint(0,len(titles) - 1)]
             + " " + names[random.randint(0,len(names) - 1)]
             + " " + names[random.randint(0,len(names) - 1)]
             + " the "
             + descriptors[random.randint(0,len(descriptors) - 1)])

    print(output)

    namesInFile.close()
    descriptorsInFile.close()
    titlesInFile.close()
                    
def loadFile(infile):
    names = infile.readlines()
    for i in range(len(names)):
        names[i] = names[i].rstrip()
    return names

main()
