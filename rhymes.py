with open('PronunciationDictionary.txt') as f:
  d = dict(x.rstrip().split(None, 1) for x in f)

inp = input("Enter word: ")

## convert word into pronounciation
import pronouncing
pron = pronouncing.phones_for_word(inp)

## search key by the value
def searchKeysByVal(dict, byVal):
    keysList = []
    itemsList = dict.items()
    for item in itemsList:
        if item[1] == byVal:
            keysList.append(item[0])
    return keysList    

## get the list of words that matches with the input word
def searchKeysByValList(itemDict, valList):
    keysList = []
    itemsList = itemDict.items()
    for item  in itemsList:
        if item[1] in valList:
            keysList.append(item[0])
    return  keysList 

keysList = searchKeysByVal(d, pron[0])
 
## iterate over the list of words
for index, company in enumerate(keysList):
    print("{}: {}".format(index, company))