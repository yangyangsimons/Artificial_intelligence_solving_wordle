import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import random
import math

def __Calculate__Entropy__Based__On__Position(wordList):
    # first calculate the probability p(x)
    probabilityList = []
    for i in range(5):
        probabilities = {}
        totalWord = len(wordList)
        for letter in ascii_lowercase:
            count = 0
            for word in wordList:
                if(word[i] == letter):
                    count = count + 1
            probabilities.update({letter : round(count/totalWord,4)}) 
        probabilities = {k: v for k, v in sorted(probabilities.items(), key=lambda item: item[1], reverse= True)}    
        probabilityList.append(probabilities)
# calculate the entropy based on probabilities
    entropyList = []
    for word in wordList:
        entropy = 0
        for j in range(len(word)):
            probability = probabilityList[j][word[j]]
            information = math.log(1/probability,2)
            entropy = entropy + probability * information

        entropyList.append(entropy)
    # print(len(entropyList))
    return entropyList


# select the word based on highest entropy
def __selectWord__(wordList,entropyList):
    selectedWord = wordList[entropyList.index(max(entropyList))]
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



successCount = 0
roundList = []
for testTimes in range(len(data.test_word_list)):
    # select the first word to guess
    entropyList = __Calculate__Entropy__Based__On__Position(data.valid_word_list,)
    FirstSelectedWord = __selectWord__(data.valid_word_list,entropyList)
    # objectWord = random.choice(data.test_word_list)
    objectWord = data.test_word_list[testTimes]

    # use a timesPlay store how many times it takes to work out the right word
    timesPlay = 0
    guessResult = ws.__feedback__(FirstSelectedWord,objectWord)
    # print(objectWord)
    # print(FirstSelectedWord)
    # print(guessResult)
    if(guessResult == ["green","green","green","green","green"]):
        print(objectWord)
        print(FirstSelectedWord)
        print(guessResult)
        successCount = successCount + 1
        print("success")
        timesPlay = 1
        roundList.append(timesPlay)
        continue
    # second guess
    newWordList = __Set__New__Word__List__(FirstSelectedWord,guessResult,data.valid_word_list)
    entropyList = __Calculate__Entropy__Based__On__Position(newWordList)
    selectedWord = __selectWord__(newWordList,entropyList)
    guessResult = ws.__feedback__(selectedWord,objectWord)
    # print(len(newWordList))
    # print(objectWord)
    # print(selectedWord)
    # print(guessResult)
    if(guessResult == ["green","green","green","green","green"]):
        print(objectWord)
        print(selectedWord)
        print(guessResult)
        successCount = successCount + 1
        print("success")
        timesPlay = 2
        roundList.append(timesPlay)
        continue

    for i in range(4):
        newWordList = __Set__New__Word__List__(selectedWord,guessResult,newWordList)
        entropyList = __Calculate__Entropy__Based__On__Position(newWordList)
        selectedWord = __selectWord__(newWordList,entropyList)
        # objectWord = objectWord = ObjectWord = random.choice(data.test_word_list)
        guessResult = ws.__feedback__(selectedWord,objectWord)
        # print(len(newWordList))
        # print(objectWord)
        # print(selectedWord)
        # print(guessResult)
        if(guessResult == ["green","green","green","green","green"]):
            print(objectWord)
            print(selectedWord)
            successCount = successCount + 1
            timesPlay = i + 2
            roundList.append(timesPlay)
            print("success")
            # round = i
            # print(selectedWord +" " + objectWord)
            # successCount = successCount + 1
            break

# get the final result
print(successCount/len(data.test_word_list))
print(sum(roundList)/len(roundList))