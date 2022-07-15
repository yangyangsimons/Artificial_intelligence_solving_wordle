import pandas as pd
from string import ascii_lowercase

data1 = pd.read_csv("/Users/lynnyang/work/wordle/data/allowed_words.txt",header=None)
data2 = pd.read_csv("/Users/lynnyang/work/wordle/data/2021_2022_answer_list.csv")
testWords = list(data2["Answer"])
allWords = list(data1[0])

test_word_list=[]
valid_word_list = []
sorted_word_list = []
for word in allWords:
    if (len(word)== 5):
# if the word has an uppercase letter, then ignore the whole word.
        if(any(letter.isupper() for letter in word)):
            continue
        else:
# sort the word in alphabet order, for example "sample" will sorted as "aelmps", this is used in the later function;
            sorted_word = "".join(sorted(word))
# add all the word length equals 5 into the valid_word_list and the sorted word into sorted_word_list;
            valid_word_list.append(word)
            sorted_word_list.append(sorted_word)

for word in testWords:
    word = word.lower()
    test_word_list.append(word)