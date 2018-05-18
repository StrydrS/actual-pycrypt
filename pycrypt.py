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