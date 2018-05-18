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
    
    
def decryptMessage(createdArray, newArray):
    
    decryptedMessage = ""
    allChars = string.printable
    
    for m in range(0, len(createdArray)):                 
        for q in range(0, len(newArray)):
            if(newArray[q] == createdArray[m]):
                decryptedMessage = decryptedMessage + allChars[q]
                
    return decryptedMessage
                    

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
        allChars = string.printable
        allNums = string.digits
        
        sortToNums = ""
        
        for x in encryptedMessage:
            for i in range(0, len(allNums)):
                if(x == allNums[i]):
                    sortToNums = sortToNums + x
        
        lenDecryptArray = len(sortToNums) // 5
        
        decryptArray = [0] * lenDecryptArray
        
        updateMax = 5
        updateMin = 0
        
        for z in range(0, lenDecryptArray):
            decryptArray[z] = int(sortToNums[updateMin:updateMax])
            updateMin = updateMin + 5
            updateMax = updateMax + 5
        
        print(decryptMessage(decryptArray, newArray))
                
                    
main()