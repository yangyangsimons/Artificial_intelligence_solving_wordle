import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import random
import math

def __Calculate__Probability__Based__On__Position(wordList):
    probabilityList = []
    for letterLength in range(5):
        probabilities = {}
        totalWord = len(wordList)
        for letter in ascii_lowercase:
            count = 0
            for word in wordList:
                if(word[letterLength] == letter):
                    count = count + 1
            probabilities.update({letter : round(count/totalWord,4)}) 
        sortedProbabilities = {k: v for k, v in sorted(probabilities.items(), key=lambda item: item[1], reverse= True)}    
        probabilityList.append(sortedProbabilities)
# calculate the entropy
    entropyList = []
    for word in wordList:
        entropy = 0
        for i in range(len(word)):
            probability = probabilityList[i][word[i]]
            information = math.log(1/probability,2)
            entropy = entropy + probability * information

        entropyList.append(entropy)
    # print(len(entropyList))
    selectedWord = wordList[entropyList.index(max(entropyList))]
    # print(word)
    return selectedWord



def __Set__New__Word__List__(selectedWord,feedback,word_list):
    yellow_dic = {}
    green_dic = {}
    grey_dic = {}
    for i in range(len(feedback)):
        if(feedback[i] == "yellow"):
            yellow_dic.update({i:selectedWord[i]})
        if(feedback[i] == "green"):
            green_dic.update({i:selectedWord[i]})
        if(feedback[i] == "grey"):
            grey_dic.update({i:selectedWord[i]})
    # calculate the new valid word list based on the feedback
    new_valid_list = []
    for word in word_list:
        letter_status = []
        for index,letter in yellow_dic.items():
            if(word.find(letter) != -1 and word[index] != letter):
                letter_status.append(True)
            else:
                letter_status.append(False)
        for index in green_dic.keys():
            if(word[index] == green_dic[index]):
                letter_status.append(True)
            else:
                letter_status.append(False)
        for letter in grey_dic.values():
            if(word.find(letter) == -1):
                letter_status.append(True)
            else:
                letter_status.append(False)
        if(all(letter_status)):
            new_valid_list.append(word)
            continue
        else:
            continue
    return new_valid_list



firstProbabilityList = __Calculate__Probability__Based__On__Position(data.valid_word_list)
FirstSelectedWord = __Calculate__Entropy__(data.valid_word_list,firstProbabilityList)
print(FirstSelectedWord)

successCount = 0
round = 0
for j in range(len(data.test_word_list)):
    objectWord = random.choice(data.test_word_list)
    guessResult = ws.__feedback__(FirstSelectedWord,objectWord)
    newWordList = __Set__New__Word__List__(FirstSelectedWord,guessResult,data.valid_word_list)
    distributionList = __Calculate__Probability__Based__On__Position(newWordList)
    selectedWord = __Calculate__Entropy__(newWordList,distributionList)
    guessResult = ws.__feedback__(selectedWord,objectWord)
    print(len(newWordList))
    print(objectWord)
    print(selectedWord)
    print(guessResult)

    for i in range(4):
        wordList = __Set__New__Word__List__(selectedWord,guessResult,newWordList)
        distributionList = __Calculate__Probability__Based__On__Position(wordList)
        selectedWord = __Calculate__Entropy__(wordList,distributionList)
        # objectWord = objectWord = ObjectWord = random.choice(data.test_word_list)
        guessResult = ws.__feedback__(selectedWord,objectWord)
        print(len(wordList))
        print(objectWord)
        print(selectedWord)
        print(guessResult)
        if(guessResult == ["green","green","green","green","green"]):
            successCount = successCount + 1
            print("success")
            round = i
            print(selectedWord +" " + objectWord)
            successCount = successCount + 1
            break