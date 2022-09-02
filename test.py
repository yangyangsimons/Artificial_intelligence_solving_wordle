import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import pandas as pd
import math

def __Calculate_Entropy__(probability_dic):
    entropy = 0
    for value in probability_dic.values():
        information = math.log(1/value,2)
        entropy = entropy + (value * information)
    return entropy

def __Calculate_probabilityDistribution__(exampleWord,wordList):
    result = []
    result_dic = {}

    for word in wordList:
        feedback = ws.__feedback__(exampleWord,word)
        subResult = "".join(feedback)

        if(result.count(subResult) != 0):
            index1 = result.index(subResult)
            # key1 = "result" + index
            result_dic[str(index1)] = result_dic[str(index1)] + 1
        else:
            result.append(subResult)
            index2 = result.index(subResult)
            # key2 = "result" + index
            result_dic[str(index2)] = 1
        # print(result_dic)
    sortedResult_dic = dict(sorted(result_dic.items(), key=lambda item: item[1],reverse=True))
    for key in sortedResult_dic.keys():
        sortedResult_dic[key] = (sortedResult_dic[key] / len(wordList))
    return sortedResult_dic

def __Calculate_EntropyList__(wordList):
    entropyList = []
    for word in wordList:
        wordProbabilityDic = __Calculate_probabilityDistribution__(word,wordList)
        wordEntropy = __Calculate_Entropy__(wordProbabilityDic)
        entropyList.append(wordEntropy)
    return entropyList



# def __Calculate__Entropy__Based__On__Position(wordList):
#     # first calculate the probability p(x)
#     probabilityList = []
#     for i in range(5):
#         probabilities = {}
#         totalWord = len(wordList)
#         for letter in ascii_lowercase:
#             count = 0
#             for word in wordList:
#                 if(word[i] == letter):
#                     count = count + 1
#             probabilities.update({letter : round(count/totalWord,4)}) 
#         probabilities = {k: v for k, v in sorted(probabilities.items(), key=lambda item: item[1], reverse= True)}    
#         probabilityList.append(probabilities)
# # calculate the entropy based on probabilities
#     entropyList = []
#     for word in wordList:
#         entropy = 0
#         for j in range(len(word)):
#             probability = probabilityList[j][word[j]]
#             information = math.log(1/probability,2)
#             entropy = entropy + (probability * information)

#         entropyList.append(entropy)
#     # print(len(entropyList))
#     return entropyList



# select the word based on highest entropy
def __selectWord__(wordList,entropyList):
    selectedWord = wordList[entropyList.index(max(entropyList))]
    return selectedWord

def __selectFirstWord():
    firstEntropyList = pd.read_csv("./data/result/validEntropyList.csv").iloc[:,1].tolist()
    maxEntropy = max(firstEntropyList)
    index = firstEntropyList.index(maxEntropy)
    firstWord = data.valid_word_list[index]
    return firstWord
    

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



successCount = 0
roundList = []
# objectWord = random.choice(data.test_word_list)
objectWord = "boozy"
# use a timesPlay store how many times it takes to work out the right word
timesPlay = 0
for i in range(20):
    if (i == 0):
        newWordList = data.valid_word_list
        selectedWord = __selectFirstWord()
    else: 
        newWordList = __Set__New__Word__List__(selectedWord,guessResult,newWordList)
        print(len(newWordList))
        entropyList = __Calculate_EntropyList__(newWordList)
        selectedWord = __selectWord__(newWordList,entropyList)
    print(selectedWord)
    guessResult = ws.__feedback__(selectedWord,objectWord)
    print(guessResult)
    print("----.....")
    if(guessResult == ["green","green","green","green","green"]):
        # print(objectWord)
        # print(selectedWord)
        successCount = successCount + 1
        timesPlay = i + 1
        roundList.append(timesPlay)
        break



