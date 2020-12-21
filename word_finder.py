#Name: Tarini Srikanth
#Instructor: Turner
#Project 4- Main

from funcs import *

def main():
    stringPuzzle = get_puzzle()
    words = get_words()
    #getting the puzzle and the words
    string3=words.split(" ")
    wordsList= list(string3)
    #turning into a list
    puzzle = turnInto10by10(stringPuzzle)
    #turning puzzle into 10 by 10
    print("Puzzle:\n")
    for listNew in puzzle:
        print(*listNew, sep="")
    print()
    #printing the final puzzle
    finalList=[]
    finalList.append(check_forwards(puzzle,wordsList))
    finalList.append(check_backwards(puzzle,wordsList))
    finalList.append(check_up(puzzle,wordsList))
    finalList.append(check_down(puzzle,wordsList))
    finalList.append(check_diagonal(puzzle,wordsList))
    #appending the list that is returned from running checks 
    #on forwards, backwards, up, down, and diagonal
    #print(finalList)
    row=0
    col=0
    count=0
    #print(finalList)
    for word in wordsList:
        count=0
        reverseWord = word[::-1]
        #for backwards and up, use reverse words
        for i in range(len(finalList)):
            for j in range(len(finalList[i])):
                if ((word == finalList[i][j]) or (reverseWord==finalList[i][j])):
                    numOfWords=0
                    count=count+1
                    for item in finalList[i]:
                        if type(item) is str:
                            numOfWords+=1
                            #checking the number of words
                    row=finalList[i][j+numOfWords]
                    col=finalList[i][j+numOfWords+numOfWords]
                    #setting the col and row numbers accordingly
                    if i==0: #forwards
                        print(word+": (FORWARD) row: "+str(row)+" column: "+str(col))
                    if i==1: #backwards
                         newCol = col +(len(finalList[i][j])-1)
                         print(word+": (BACKWARD) row: "+str(row)+" column: "+str(newCol))
                    if i==2:#up
                        newCol = col +(len(finalList[i][j])-1)
                        print(word+": (UP) row: "+str(newCol)+" column: "+str(row))
                    if i==3:#down
                        print(word+": (DOWN) row: "+str(col)+" column: "+str(row))
                    if i==4:#diagonal
                        print(word+": (DIAGONAL) row: "+str(row)+" column: "+str(col))
        if count==0:
            #if no word is found
            print(word+": word not found")
            


                        

                   
            

                


    #puzzle = turnInto10by10(stringWords)
    
    #listOfWordsToSearch = list(string3)
    #print(check_backwards(puzzle,listOfWordsToSearch))
    #print(check_up(puzzle,listOfWordsToSearch))
    #print(check_down(puzzle,listOfWordsToSearch))
    #print(check_diagonal(puzzle,listOfWordsToSearch))
    #listOfMatches = getListOfMatchingWords(puzzle,listOfWordsToSearch)
    #print(listOfMatches)
    #print(getRow(listOfMatches,puzzle,listOfWordsToSearch))
    

    

if __name__ == '__main__':
    main()
            

