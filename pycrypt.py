import string
import random
 
# ================================================================== #
 
def generateNumber():
    #for each call it sets the value of newIntegers to None
    newIntegers = ""
     
    #adds new integer to the end of our integer list
    for x in range(0,255):
        newIntegers = newIntegers + str(random.randint(1,9))
     
    #sets new variable as equal to an integer of the random numbers
    newInt = int(newIntegers)
     
    #returns list of 255 integers
    return newInt
 
# ================================================================== #
 
def generateList():
    #generates list of all printable characters
    allChars = string.printable
     
    #new variable for the length of the printable characters
    lenArray = len(allChars)
    #new array generated that is the length of all printable characters
    totalArray = [0] * lenArray
    #assigns each index of totalArray to the return value of generateNumber()
    for i in range (0, lenArray):
        totalArray[i] = generateNumber()
     
    #returns filled array of random integers
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
    # random.seed function generates the same list of random numbers as long as the seed stays the same
    userSeed = int(input("What is your seed?"))
    random.seed(userSeed)
     
    #gives user the choice of wheter to decrypt or encrypt
    if(userChoice == "encrypt"):
        #newArray variable assigned to return value of generateList
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