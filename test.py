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
                if(letter in yellow_dic.values() or letter in green_dic.values()):
                    letter_status.append(True)
                else:
                    letter_status.append(False)
        if(all(letter_status)):
            new_valid_list.append(word)
            continue
        else:
            continue
    return new_valid_list

def __User__Feedback__():
    feedback = input()
    guessResult = []
    for index in range(len(feedback)):
        if(int(feedback[index]) == 0):
            guessResult.append("grey")
        if(int(feedback[index]) == 1):
            guessResult.append("yellow")
        if(int(feedback[index]) == 2):
            guessResult.append("green")
    return guessResult
# select the first word to guess
entropyList = __Calculate__Entropy__Based__On__Position(data.valid_word_list,)
FirstSelectedWord = __selectWord__(data.valid_word_list,entropyList)
print(FirstSelectedWord)
# objectWord = "angry"

print(FirstSelectedWord)
guessResult = __User__Feedback__()
print(guessResult)
# second guess
newWordList = __Set__New__Word__List__(FirstSelectedWord,guessResult,data.valid_word_list)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList)
selectedWord = __selectWord__(newWordList,entropyList)
print(selectedWord)

# feedback1 = input()
# guessResult1 = []
# for index1 in range(len(feedback1)):
#     if(int(feedback1[index1]) == 0):
#         guessResult1.append("grey")
#     if(int(feedback1[index1]) == 1):
#         guessResult1.append("yellow")
#     if(int(feedback1[index1]) == 2):
#         guessResult1.append("green")
# print(guessResult1)

guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)
# print(len(newWordList))
# print(selectedWord)
# print(guessResult)
guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)

guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)

guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)

guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)

guessResult1 = __User__Feedback__()
print(guessResult1)
newWordList2 = __Set__New__Word__List__(selectedWord,guessResult1,newWordList)
entropyList = __Calculate__Entropy__Based__On__Position(newWordList2)
selectedWord = __selectWord__(newWordList2,entropyList)
print(selectedWord)
# for i in range(4):
#     newWordList = __Set__New__Word__List__(selectedWord,guessResult,newWordList)
#     entropyList = __Calculate__Entropy__Based__On__Position(newWordList)
#     selectedWord = __selectWord__(newWordList,entropyList)
#     # objectWord = objectWord = ObjectWord = random.choice(data.test_word_list)
#     guessResult = ws.__feedback__(selectedWord,objectWord)
#     print(len(newWordList))
#     print(objectWord)
#     print(selectedWord)
#     print(guessResult)
#     if(guessResult == ["green","green","green","green","green"]):
#         # successCount = successCount + 1
#         print("success")
#         # round = i
#         # print(selectedWord +" " + objectWord)
#         # successCount = successCount + 1
#         break
