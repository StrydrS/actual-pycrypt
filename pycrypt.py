import string
import random

def generateNumber():
    newString = ""
    
    for x in range(0,5):
        newString = newString + str(random.randint(1,9))
        
    newInt = int(newString)
    return newInt
    
def generateList():
    
    allChars = string.printable
    
    lenArray = len(allChars)
    totalArray = [0]*lenArray
    for i in range (0, lenArray):
        totalArray[i] = generateNumber()
    
    return totalArray
    
def checkMessage(arrayVar, userMessage):
    allChars = string.printable
    encryptedList = [0] * len(userMessage)
    for x in range(0, len(allChars)):
        for i in range(0, len(userMessage)):
            if(allChars[x] == userMessage[i]):
                encryptedList[i] = int(arrayVar[x])
                
    file = open("output.txt", "w") 
 
    file.write(str(encryptedList))
 
    file.close() 
    
    print("Your message has been encrypted.")

def readFile():
    file = open("output.txt", "r")
      
    newVar = file.read()
    
    file.close()
    
    return newVar
    
    
                
def main():
    userChoice = str(input("Do you want to encrypt or decrypt?"))
    
    userSeed = int(input("What is your seed?"))
    random.seed(userSeed)
    
    newArray = generateList()
    
    if(userChoice == "encrypt"):
        userMessage = str(input("What is the message you want to encrypt?"))
        
        checkMessage(newArray, userMessage)
        
    elif(userChoice == "decrypt"):
        encryptedMessage = readFile()
        allNums = string.digits
        newString = ""
        
        for x in encryptedMessage:
            for i in range(0, len(allNums)):
                if(x == allNums[i]):
                    newString = newString + x
        
        lenNewArray = len(newString) // 5
        
        reallyNewArray = [0] * lenNewArray
        
        newVal = 5
        newNewVal = 0
        for z in range(0, lenNewArray):
            reallyNewArray[z] = int(newString[newNewVal:newVal])
            newVal = newVal + 5
            newNewVal = newNewVal + 5

            
        print(reallyNewArray)
        
                
                    
main()