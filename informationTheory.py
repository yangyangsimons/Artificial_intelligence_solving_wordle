import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import pandas as pd
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
            entropy = entropy + (probability * information)

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
                break
        for index in green_dic.keys():
            if(word[index] == green_dic[index]):
                letter_status.append(True)
            else:
                letter_status.append(False)
                break
        for index,letter in grey_dic.items():
            if(word.find(letter) == -1):
                letter_status.append(True)
            else:
                if(letter in yellow_dic.values() or letter in green_dic.values() and word[index] != letter):
                    letter_status.append(True)
                else:
                    letter_status.append(False)
                    break
        if(all(letter_status)):
            new_valid_list.append(word)
            continue
        else:
            continue
    return new_valid_list


def __PlayAndCount__(dataset,maxRoundAllowed):
    successCount = 0
    roundList = []
    for testTimes in range(len(dataset)):
        # objectWord = random.choice(data.test_word_list)
        objectWord = dataset[testTimes]
        # use a timesPlay store how many times it takes to work out the right word
        timesPlay = 0
        for i in range(maxRoundAllowed):
            if (i == 0):
                newWordList = data.valid_word_list
                # selectedWord = "tares"
                # guessResult = ws.__feedback__(selectedWord,objectWord)
            else: 
                newWordList = __Set__New__Word__List__(selectedWord,guessResult,newWordList)
            entropyList = __Calculate__Entropy__Based__On__Position(newWordList)
            selectedWord = __selectWord__(newWordList,entropyList)
            guessResult = ws.__feedback__(selectedWord,objectWord)
            if(guessResult == ["green","green","green","green","green"]):
                # print(objectWord)
                # print(selectedWord)
                successCount = successCount + 1
                timesPlay = i + 1
                roundList.append(timesPlay)
                if(i <= 1):
                    print("best: ", i)
                    print(selectedWord,objectWord)
                # if(i > 5):
                #     print("worst:",i)
                #     print(selectedWord,objectWord)
                break

    return roundList,successCount
# wordleAnswerRoundList,successCount = __PlayAndCount__(data.test_word_list,12)
# print(successCount/len(data.test_word_list))
# print(max(wordleAnswerRoundList))
# print(sum(wordleAnswerRoundList)/len(wordleAnswerRoundList))
# df = pd.DataFrame(wordleAnswerRoundList)
# df.to_csv("./data/result/information-wordleAnswerlist.csv")

print("-----------------")
validWordsRoundList,validSuccessCount = __PlayAndCount__(data.valid_word_list,20)
print(validSuccessCount/len(data.valid_word_list))
maxValue = max(validWordsRoundList)
maxValueIndex = validWordsRoundList.index(maxValue)
print(data.valid_word_list[maxValueIndex])
print(sum(validWordsRoundList)/len(validWordsRoundList))
df = pd.DataFrame(validWordsRoundList)
df.to_csv("./data/result/information-validWordList.csv")