<<<<<<< HEAD
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
=======
import random

def generateList():
    
    
def generateNumber():
    newString = ""
    for x in range(0,5):
        newString = newString + str(random.randint(0,9))
    newInt = int(newString)

def main():
    userSeed = int(input("What is your seed?"))
    random.seed(userSeed)
    
    generateList()
    
    
    
    
main()
>>>>>>> 0b3a32a91495649972c2fb4b5a80c06899ea4219
