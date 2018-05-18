import string
import random
def generateList():
    
    allChars = string.printable
    
    lenArray = len(allChars)
    totalArray = [0]*lenArray
    for i in range (0, lenArray):
        totalArray[i] = 54235
    print(totalArray)
    print(lenArray)
    print(allChars)
    
def main():
    generateList()

main()
