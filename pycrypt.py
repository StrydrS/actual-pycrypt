import string
import random

# ================================================================== #

def generateNumber():
    newString = ""
    
    for x in range(0,255):
        newString = newString + str(random.randint(1,9))
        
    newInt = int(newString)
    return newInt

# ================================================================== #

def generateList():
    
    allChars = string.printable
    
    lenArray = len(allChars)
    totalArray = [0]*lenArray
    for i in range (0, lenArray):
        totalArray[i] = generateNumber()
    
    return totalArray

# ================================================================== #

def checkMessage(arrayVar, userMessage):
    allChars = string.printable
    encryptedList = [0] * len(userMessage)
    for x in range(0, len(allChars)):
        for i in range(0, len(userMessage)):
            if(allChars[x] == userMessage[i]):
                encryptedList[i] = int(arrayVar[x])
     
    fileName = str(input("What is your file name?"))
    
    file = open(fileName, "w") 
 
    file.write(str(encryptedList))
 
    file.close() 
    
    print("Your message has been encrypted.")

# ================================================================== #

def readFile():
    fileName = str(input("What is your file name?"))
    
    file = open(fileName, "r")
      
    newVar = file.read()
    
    file.close()
    
    return newVar

# ================================================================== #
    
def decryptMessage(createdArray, newArray):
    
    decryptedMessage = ""
    allChars = string.printable
    
    for m in range(0, len(createdArray)):                 
        for q in range(0, len(newArray)):
            if(newArray[q] == createdArray[m]):
                decryptedMessage = decryptedMessage + allChars[q]
                
    return decryptedMessage

# ================================================================== #

def undoFile():
    encryptedMessage = readFile()
    allChars = string.printable
    allNums = string.digits
        
    sortToNums = ""
        
    for x in encryptedMessage:
        for i in range(0, len(allNums)):
            if(x == allNums[i]):
                sortToNums = sortToNums + x
                
    return sortToNums
# ================================================================== #
def beginDecryption(sortToNums):
    lenDecryptArray = len(sortToNums) // 255
        
    decryptArray = [0] * lenDecryptArray
        
    updateMax = 255
    updateMin = 0
        
    for z in range(0, lenDecryptArray):
        decryptArray[z] = int(sortToNums[updateMin:updateMax])
        updateMin = updateMin + 255
        updateMax = updateMax + 255
        
    return decryptArray

# ================================================================== #

def main():
    userChoice = str(input("Do you want to encrypt or decrypt?"))
    
    userSeed = int(input("What is your seed?"))
    random.seed(userSeed)
    
    if(userChoice == "encrypt"):
        
        newArray = generateList()
        
        userMessage = str(input("What is the message you want to encrypt?"))
        
        checkMessage(newArray, userMessage)
        
    elif(userChoice == "decrypt"):
        
        newArray = generateList()
        
        sortToNums = undoFile()
        
        decryptArray = beginDecryption(sortToNums)
 
        decrypted = decryptMessage(decryptArray, newArray)
        
        print("Your decrypted message is '", decrypted, "'.", sep="")
                                   
main()