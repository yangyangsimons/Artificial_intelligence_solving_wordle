
import Data_Processing as data
import termcolor as colored
import random


def __validWord__(answer):
    if(len(answer) > 5):
        # print("5 letters only")
        return False
    else:
        if(answer in data.valid_word_list):
            return True
        else:
            # print("This is not a valid word")
            return False

def __feedback__(userWord, targetWord):
    validWord = __validWord__(userWord)
    color = []
    if(validWord):
        for i in range(len(targetWord)):
            # check if this letter is in target word
            if(userWord[i] in targetWord):
                if (userWord[i] == targetWord[i]):
                    color.append("green")
                else:
                    color.append("yellow")
            else:
                color.append("grey")
    return color

