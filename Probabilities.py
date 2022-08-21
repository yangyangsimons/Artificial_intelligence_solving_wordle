import Wordle_Simulation as ws
import Data_Processing as data
from string import ascii_lowercase
import random

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

successCount = 0

for i in range(len(data.test_word_list)):
    objectWord = random.choice(data.test_word_list)
    # word_list = data.valid_word_list
    # letterFrequency = __Calculate_Frequency__(word_list)
    # # print(sortedLettersBasedOnFrequency)
    # selectedWord= __Select_Word__(letterFrequency,word_list)
    # # print(selectedWord)
    # # print(objectWord)
    # guessResult = ws.__feedback__(selectedWord,objectWord)
    # # print(guessResult)
    # if(guessResult == ["green","green","green","green","green"]):
    #     # print("success")
    #     print(selectedWord +" " + objectWord)
    #     successCount = successCount + 1
    #     break

    for i in range(6):
        if( i == 0):
            word_list = data.valid_word_list
        else:
            word_list  = __Set__New__Word__List__(selectedWord,guessResult,word_list)
        # print(len(word_list))
        letterFrequency = __Calculate_Frequency__(word_list)
        # print(sortedLettersBasedOnFrequency)
        selectedWord = __Select_Word__(letterFrequency,word_list)
        # print(selectedWord)
        # print(objectWord)
        guessResult = ws.__feedback__(selectedWord,objectWord)
        # print(guessResult)
        if(guessResult == ["green","green","green","green","green"]):
            successCount = successCount + 1
            break
        else:
            if(i == 5):
                print(selectedWord,objectWord)

print(successCount/len(data.test_word_list))