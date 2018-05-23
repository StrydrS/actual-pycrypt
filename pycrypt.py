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
    
    #sets all characters as a variable
    allChars = string.printable
    
    #sets new list the length of the message
    encryptedList = [0] * len(userMessage)
    
    #for loop iterates the length of all printable characters
    for x in range(0, len(allChars)):
        #for loop iterates the length of the user's message
        for i in range(0, len(userMessage)):
            #if iteration of the character loop is equal to iteration of the user message
            if(allChars[x] == userMessage[i]):
                #fills encryptedList with integer from the printable character index of the generated list
                encryptedList[i] = int(arrayVar[x])
    
    #variable that allows user to 
    doToFile("w", encryptedList)
     
    print("Your message has been encrypted.")
 
# ================================================================== #
 
def doToFile(rw, encryptedList):
    #asks user for file name input
    fileName = str(input("What is your file name?"))
    #if the function is called for a "read"
    if(rw == "r"):
        #file opens user input file name and reads it
        file = open(fileName, "r")
        #fileReturn is set to the read value of file
        fileReturn = file.read()
        #file is closed
        file.close()
        
        #returns the read value of the file, or a list of integers representing the user's encrypted message
        return fileReturn
    
    #if the function is called for a "write"
    elif(rw == "w"):
        #file is opened and wiped
        file = open(fileName, "w")
        #file is written with the return value of the encryptedList, or the user's encrypted message
        file.write(str(encryptedList))
        #file is closed
        file.close()
        
 
# ================================================================== #
     
def decryptMessage(createdArray, newArray):
    #initializes decryptedMessage
    decryptedMessage = ""
    #sets allChars as equal to all printable characters
    allChars = string.printable
    
    #iterates through the length of createdArray, or the decrypted array from the encrypted text file
    for m in range(0, len(createdArray)):
        #iterates through the length of the newArray, or every printable character
        for q in range(0, len(newArray)):
            #if index q of every printable character is equal to index m of our decrypted array
            if(newArray[q] == createdArray[m]):
                #add the decrypted character to the decrypted message string
                decryptedMessage = decryptedMessage + allChars[q]
                
    #returns the finished, decrypted message
    return decryptedMessage
 
# ================================================================== #
 
def undoFile():
    #encrypted message set to the return value of doToFile, or a list of integers representing the user's encrypted message
    encryptedMessage = doToFile("r", 1)
    #allChars is set to a list of all printable characters
    allChars = string.printable
    #allNums is set to a list of all numbers, 0-9
    allNums = string.digits
    
    #sortToNums is set to an empty string
    sortToNums = ""
    
    #iterates the values of the encrypted message
    for x in encryptedMessage:
        #iterates the length of all numbers 0-9
        for i in range(0, len(allNums)):
            #if the value in the encrypted message is a number, it is extracted and added to the string sortToNums
            if(x == allNums[i]):
                sortToNums = sortToNums + x
    
    #sortToNums, or a string of integers representing encrypted message
    return sortToNums
 
# ================================================================== #
 
def beginDecryption(sortToNums):
    #the length of the decryption array is set to the length of the encrypted string divided by 255, or the number of characters 
    lenDecryptArray = len(sortToNums) // 255
    
    #decryptArray is set as an empty array with the length of lenDecryptArray
    decryptArray = [0] * lenDecryptArray
    
    #initializes the minimum and maximum values for extraction to a list
    updateMax = 255
    updateMin = 0
    
    #for loop iterates the length of the lenDecryptArray
    for z in range(0, lenDecryptArray):
        #decryptArray[z] is set to the spliced string, or one "letter" in our decryption
        decryptArray[z] = int(sortToNums[updateMin:updateMax])
        #updates minimum and maximum to fill array
        updateMin = updateMin + 255
        updateMax = updateMax + 255
    
    #returns decrypted array
    return decryptArray
 
# ================================================================== #
 
def main():
    userChoice = str(input("Do you want to encrypt or decrypt?"))
    # random.seed function generates the same list of random numbers as long as the seed stays the same
    userSeed = int(input("What is your seed?"))
    random.seed(userSeed)
     
    #gives user the choice of wheter to decrypt or encrypt
    if(userChoice == "encrypt"):
        #newArray variable assigned to return value of generateList, or a list of 255 random integers per printable character
        newArray = generateList()
        #asks user for message they want to input
        userMessage = str(input("What is the message you want to encrypt?"))
        #checkmessage function takes in the generated list and the message you want to encrypt
        checkMessage(newArray, userMessage)
         
    elif(userChoice == "decrypt"):
        #newArray variable assigned to return value of generateList, or a list of 255 random integers per printable character
        newArray = generateList()
        #creates new variable set to the list of numbers returned by undoFile, or a list of integers representing the encrypted message.
        sortToNums = undoFile()
        #decryptArray is set to the return value of beginDecryption with the parameter of sortToNums, or the decrypted array to match to the generated list
        decryptArray = beginDecryption(sortToNums)
        #decrypted is set to the return value of decryptMessage with parameters decryptArray and newArray
        decrypted = decryptMessage(decryptArray, newArray)
         
        print("Your decrypted message is '", decrypted, "'.", sep="")
                                    
main()