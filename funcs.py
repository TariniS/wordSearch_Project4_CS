#Name: Tarini Srikanth
#Instructor Clark Turner
#Project: 4-Funcs.py

def convertStringIntoList(words):
    words.split(" ")
    return [character for character in words]
    #takes a string of words and returns a list

def turnInto10by10(stringOfCharacters):
    #converts a string of 100 characters into a double array of 10 rows and columns
    listOfStrings = convertStringIntoList(stringOfCharacters)
    list0=[]
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    #making 10 lists and a final list
    finalList =[]
    for i in range(100):
        if i<10:
            list0.append(listOfStrings[i])
        elif i<20:
            list1.append(listOfStrings[i])
        elif i<30:
            list2.append(listOfStrings[i])
        elif i<40:
            list3.append(listOfStrings[i])
        elif i<50:
            list4.append(listOfStrings[i])
        elif i<60:
            list5.append(listOfStrings[i])
        elif i<70:
            list6.append(listOfStrings[i])
        elif i<80:
            list7.append(listOfStrings[i])
        elif i<90:
            list8.append(listOfStrings[i])
        elif i<100:
            list9.append(listOfStrings[i])
        else:
            i=i
        #splitting the array by 10's and adding to the appropriate list number
    finalList.append(list0)
    finalList.append(list1)
    finalList.append(list2)
    finalList.append(list3)
    finalList.append(list4)
    finalList.append(list5)
    finalList.append(list6)
    finalList.append(list7)
    finalList.append(list8)
    finalList.append(list9)
    #adding all the lists to the final list
    return finalList

def checkInARowForward(list1,wordsList):
    #based on a puzzle and a words list, check if a word is there in the 
    #horizontal direction
    listOfWords=[]
    string1=""
    for item in wordsList:
        for char in list1:
             string1=string1+char
             #creating a string of the entire row
        if item in string1:
            listOfWords.append(item)
            #checking if the string in in the words list
    return listOfWords

def getRow(listOfI,puzzle,words):
    #gets the row based on the puzzle
    rowList=[]
    for i in range(len(listOfI)):
        for j in range(len(listOfI[i])):
            if len(listOfI[i][j])!=0:
                rowList.append(i)
    return rowList

def getCol(list1,puzzle,words):
    #getting the column number
    numOfWords=0
    row=[]
    col=[]
    finalList=[]
    newList=[]
    index=0
    for item in list1:
        if type(item) is str:
            numOfWords=numOfWords+1
            #checking how many words there are
    for i in range(numOfWords):
        row = list1[i+numOfWords]
        newList = puzzle[row]
        Nstring=""
        for j in range(len(newList)):
            Nstring = Nstring+newList[j]
            #creating a string that reprsents each item in a specific col
        index=Nstring.index(list1[i])
        col.append(index)
    finalList.append(col)
    return flattenList(finalList)

def check_forwards(puzzle,words):
    #checking if a word is there horizontally
    finalList=[]
    rowList=[]
    colList=[]
    for i in range(len(puzzle)):
        finalList.append(checkInARowForward(puzzle[i],words))
        #using the previous method to check
    rowList=getRow(finalList,puzzle,words)
    finalList.append(rowList)
    finalList = flattenList(finalList)
    colList=getCol(finalList,puzzle,words)
    #getting row and column based on the methods
    finalList.append(colList)
    return flattenList2(finalList)

def check_backwards(puzzle,words):
    #checking in the backwards direction
    listOfWords = reverseWordsInList(words)
    #reversing the words in the string 
    finalList=[]
    for i in range(len(puzzle)):
        finalList.append(checkInARowForward(puzzle[i],listOfWords))
    #rowList=getRow(finalList,puzzle,listOfWords)
    #finalList.append(rowList)
    rowList=getRow(finalList,puzzle,words)
    finalList.append(rowList)
    finalList = flattenList(finalList)
    colList=getCol(finalList,puzzle,words)
    finalList.append(colList)
    #getting row and column
    return flattenList2(finalList)
    #newList= check_forwards(puzzle,listOfWords)
    #return reverseWordsInList(newList)

def check_up(puzzle,words):
    #checking in the up direction
    newPuzzle=convertColsIntoRows(puzzle)
    #converting the list and transposing so that columns are rows
    listOfWords = reverseWordsInList(words)
    finalList=[]
    rowList=[]
    for i in range(len(newPuzzle)):
        finalList.append(checkInARowForward(newPuzzle[i],listOfWords))
    rowList=getRow(finalList,newPuzzle,words)
    finalList.append(rowList)
    finalList = flattenList(finalList)
    colList=getCol(finalList,newPuzzle,words)
    #getting the row and column number
    finalList.append(colList)
    return flattenList2(finalList)
    

def check_down(puzzle,words):
    #checking the downwards direction
    newPuzzle = convertColsIntoRows(puzzle)
    finalList=[]
    rowList=[]
    colList=[]
    for i in range(len(newPuzzle)):
        finalList.append(checkInARowForward(newPuzzle[i],words))
    rowList=getRow(finalList,newPuzzle,words)
    finalList.append(rowList)
    finalList = flattenList(finalList)
    colList=getCol(finalList,newPuzzle,words)
    #getting the row and col and appending it
    finalList.append(colList)
    return flattenList2(finalList)
    #for i in range(len(newPuzzle)):
        #finalList.append(checkInARowForward(newPuzzle[i],words))
    #rowList=getRow(finalList,newPuzzle,words)
    #finalList.append(rowList)
    #return flattenList(finalList)

def check_diagonal(puzzle,words):
    newList = getDiagonalList(puzzle,words)
    #transposing diagonal words to be rows horizontally
    finalList=[]
    rowList=[]
    colList=[]
    for i in range(len(newList)):
        finalList.append(checkInARowForward(newList[i],words))
    #finalList2=flattenList2(finalList)
    #for i in range(len(words)):
        #for j in range(len(newList)):
            #newString=""
            #for r in range(len(newList[j])):
                #newString = newString+newList[j][r]
            #if words[i] in newString:
                #colList.append(newString.index(words[i]))
    rowList=getRow(finalList,newList,words)
    finalList.append(rowList)
    finalList = flattenList(finalList)
    colList=getCol(finalList,newList,words)
    #same logic as forward, checking rows and col
    finalList.append(colList)
    #for w in range(len(words)):
            #for r in range(len(newList)):
                #newString=""
                #for q in range(len(newList[r])):
                    #newString = newString + newList[r][q]
                #if words[w] in newString:
                    #rowList.append(newString.index(words[w]))
    return flattenList2(finalList)

def getDiagonalList(puzzle,words):
    #convering a diagonal list into horizontal
    row = 0
    col = 0
    finalList = []
    for i in range(10):
        diagList=[]
        x = 10-i
        #going through 10 times
        tempRow = row
        tempCol = col
        for j in range(x):
            diagList.append(puzzle[tempRow][tempCol])
            tempRow +=1
            tempCol+=1
            #incrementing
        row = row + 1
        finalList.append(diagList)
    #for the left side..
    row = 0
    col = 1
    for i in range(9):
        diagList=[]
        x = 9-i
        tempRow = row
        tempCol = col
        for j in range(x):
            diagList.append(puzzle[tempRow][tempCol])
            tempRow +=1
            tempCol+=1
        col = col + 1
        finalList.append(diagList)

    
    return finalList

def reverseWordsInList(listOfwords):
    #used for the backwards and up direction
    #takes the list and reverses the strings inside
    newList=[]
    for aString in listOfwords:
        newList.append(aString[::-1])
    return newList


def flattenList(listOfList):
    return[j for sub in listOfList for j in sub]
    #used to help iterate through the list

def convertColsIntoRows(listOfLists):
    #program to transpose the columns into horizontal rows
    newColsList=[]
    for i in range(len(listOfLists)):
        newCol=[]
        for j in range(len(listOfLists[i])):
            newCol.append(listOfLists[j][i])
        newColsList.append(newCol)
    return newColsList

def getListOfMatchingWords(puzzle,words):
    finalList=[]
    forwardList=check_forwards(puzzle,words)
    backwardsList = check_backwards(puzzle,words)
    upList = check_up(puzzle,words)
    downList = check_down(puzzle,words)
    diagonalList = check_diagonal(puzzle,words)
    finalList.append(forwardList)
    finalList.append(backwardsList) 
    finalList.append(upList)
    finalList.append(downList)
    finalList.append(diagonalList)
    return finalList

def flattenList2(listOfLists):
    #used to help with iterating
    newList=[]
    for item in listOfLists:
        if type(item) is list:
            for item2 in item:
                newList.append(item2)
        else:
            newList.append(item)
    return newList
    #returns a 1d array

def get_puzzle():
    stringPuzzle = input("")
    return stringPuzzle
    #user input for the puzzle
def get_words():
    words = input("")
    return words
    #user input for the words list

    








    




   


