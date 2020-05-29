"""
Author: Professor Floyd & Heather Hickman
Program name: hh_9_5 - chapter 9 exercise 5, "Word Frequency"
Date: 3/11/19
Summary: The program takes in a text file, reads it, and uses the set method to split the text file into a list of unique words.
            It then prints out that dictionary with the words as the key and the number of times the word appears in the document
            as the values.

1. VARIABLES
    wordCount, inFile, fileName, inText, wordList,

2. INPUTS
    fileName - if user does not want to enter a text file, they can hit ENTER to use the default text.txt file.

3. PROCESSES
    a. Prompt the user for a file, allow user to press enter to use the default file text.txt.
    b. Open the file for reading, enter the words into a list using the split method.
    c. Close the file.
    d. Remove punctuation from the list using a for loop and the strip method, also change all words into
        lowercase so that the set method will not consider punctuated or Proper capped words as separate unique words.
    e. Put the list into a set.
    f. Use a for loop to count the number of times each unique word is repeated in the set.

4. OUTPUTS
    a. Display the dictionary keys and values with a header.

"""
def main():
    # inputs / variables
    wordCount   =   {}          # define a dictionary to hold our words (keys) & their associates counts (values)

    # prompt the user for a file
    fileName    =   input("Please enter a file name to process (press ENTER for default text.txt:\t")
    if fileName == None or fileName == '':      # nothing entered, set a default fileName
        fileName = 'text.txt'

    # open file for reading
    inFile = open(fileName, 'r')

    # read the file into a list
    inText = inFile.read()

    # use the split method to create a list of words from our text file
    wordList = inText.split()

    # close the file
    inFile.close()

    # processing & outputs

    # remove punctuation from our wordList
    for index in range(len(wordList)):
        # strip out punctuation
        wordList[index] = wordList[index].strip('.,')
        wordList[index] = wordList[index].strip('.')
        wordList[index] = wordList[index].strip(',')
        # if we want a case insensitive count, we convert all words to lower
        wordList[index] = wordList[index].lower()

    # create a set called uniqueWordSet that we can use to process
    uniqueWordSet = set(wordList)

    # loop / interate our UniqueWordList and initialize our wordCount{} to 0.
    for word in uniqueWordSet:
        wordCount[word] = 0

    # for each word in the text, increase its counter
    for word in wordList:
        wordCount[word] += 1

    # print results
    print("-" * 50)
    print(format('Word','15'), '\t',format('Occurences','15'))
    print("-" * 50)

    # loop our dictionary and pop each key value pair off, then output to screen
    while len(wordCount):
        wordKeyValueTuple = wordCount.popitem()
        print(format(wordKeyValueTuple[0],'15'),format(wordKeyValueTuple[1],'15'))

main()