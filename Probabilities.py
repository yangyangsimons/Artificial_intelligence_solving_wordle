import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import random
import pandas as pd

# calculate the frequency of all(26) letters
def __Calculate_Frequency__(wordList):
    str = "".join(wordList)
    tempFrequency = {}
    totalNumberStr = len(str)
    for i in ascii_lowercase:
        tempFrequency[i] = round(str.count(i)/totalNumberStr, 4)
    return tempFrequency

# Choose the five most frequently occurring letters
def __Select_Word__(letter_frequency,word_List):
    word_Frequency_List = []
    for word in word_List:
        wordFrequency = 0
        for i in range(len(word)):
            wordFrequency = wordFrequency + letter_frequency[word[i]]       
        word_Frequency_List.append(wordFrequency)
    selectedWord = word_List[word_Frequency_List.index(max(word_Frequency_List))]
    return selectedWord

#recalculate the word frequency based on the result
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
        for index,letter in grey_dic.items():
            if(word.find(letter) == -1):
                letter_status.append(True)
            else:
                if(letter in yellow_dic.values() or letter in green_dic.values() and word[index] != letter):
                    letter_status.append(True)
                else:
                    letter_status.append(False)
        if(all(letter_status)):
            new_valid_list.append(word)
            continue
        else:
            continue
    return new_valid_list


def __PlayAndCount__(dataset,maxRoundAllowed):
    successCount = 0
    roundList = []
    for i in range(len(dataset)):
        objectWord = dataset[i]
        # use a timesPlay store how many times it takes to work out the right word
        timesPlay = 0
        for i in range(maxRoundAllowed):
            if( i == 0):
                word_list = data.valid_word_list
            else:
                word_list  = __Set__New__Word__List__(selectedWord,guessResult,word_list)
            # print(len(word_list))
            letterFrequency = __Calculate_Frequency__(word_list)
            # print(sortedLettersBasedOnFrequency)
            selectedWord = __Select_Word__(letterFrequency,word_list)
            # print(objectWord)
            guessResult = ws.__feedback__(selectedWord,objectWord)
            # print(guessResult)
            if(guessResult == ["green","green","green","green","green"]):
                successCount = successCount + 1
                timesPlay = i + 1
                roundList.append(timesPlay)
                if(i <= 1):
                    print("best: ", i)
                    print(selectedWord,objectWord)
                if(i >= maxRoundAllowed - 4):
                    print("worst:",i)
                    print(selectedWord,objectWord)
                break
            # else:
            #     if(i >= maxRoundAllowed - 3):
            #         print("maybe worst:" + i)
            #         print(selectedWord,objectWord)
    return roundList,successCount

wordleAnswerRoundList,successCount = __PlayAndCount__(data.test_word_list,13)
print(successCount/len(data.test_word_list))
print(max(wordleAnswerRoundList))
print(sum(wordleAnswerRoundList)/len(wordleAnswerRoundList))
df = pd.DataFrame(wordleAnswerRoundList)
df.to_csv("./data/result/probability-wordleAnswerlist.csv")
# print("-----------------")
# validWordsRoundList,validSuccessCount = __PlayAndCount__(data.valid_word_list,20)
# print(validSuccessCount/len(data.valid_word_list))
# print(max(validWordsRoundList))
# print(sum(validWordsRoundList)/len(validWordsRoundList))
# df = pd.DataFrame(validWordsRoundList)
# df.to_csv("./data/result/probability-validWordList.csv")
