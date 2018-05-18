import string
import random

def generateNumber():
    newString = ""
    
    for x in range(0,5):
        newString = newString + str(random.randint(0,9))
        
    newInt = int(newString)
    return newInt
    
def generateList():
    
    allChars = string.printable
    
    lenArray = len(allChars)
    totalArray = [0]*lenArray
    for i in range (0, lenArray):
        totalArray[i] = generateNumber()
    print(totalArray)
    
def main():
    generateList()

main()