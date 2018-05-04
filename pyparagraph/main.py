#import modules 
import os

#open text file to read 
fname = open("paragraph_1.txt", "r")
patxt = fname.read()

#check if file read 
print(patxt)

#title activity 
print("Paragraph Analysis")
print("-------------------------------------------")

#Assess passage for approximate word count 
from collections import Counter
wordcounts = []

# define and count sentences 
sentences = patxt.split('.')
sent_count = patxt.count('.')
print("total sentences: ", sent_count)


#Loop through sentences to count words 
import re
for sentence in sentences: 
    words = sentence.split(' ')
    wordcounts.append(len(words))

# and get count for letters in passage
    letters = [letter for letter in patxt]
    lettercount = len(letters)

#check point 
print(lettercount)
print(wordcounts)
print(sum(wordcounts))

#calculate average sentence length in words 
avg_sentlen = sum(wordcounts)/sent_count
print(str(avg_sentlen))

#calculate average letter count per word



