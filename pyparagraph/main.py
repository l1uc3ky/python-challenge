#import modules 
import os

#open text file to read 
fname = open("paragraph_1.txt", "r")
patxt = fname.read()

#check if file read 
#print(patxt)

#title activity 
print("Paragraph Analysis")
print("-------------------------------------------")

#Assess passage for approximate word count 
from collections import Counter
wordcounts = []

# define and count sentences 
sentences = patxt.split('.')
sent_count = patxt.count('.')
print("Approximate Sentence Count: ", sent_count)


#Loop through sentences to count words 
import re
for sentence in sentences: 
    words = sentence.split(' ')
    wordcounts.append(len(words))
    total_words = sum(wordcounts)

# and get count for letters in passage
    letters = [letter for letter in patxt]
    lettercount = len(letters)

#check point 
#print(lettercount)
#print(wordcounts)
print("Approximate Word Count: ", total_words)

#calculate average sentence length in words 
avg_sentlen = (sum(wordcounts)/sent_count)
print("Average Sentence Length: " + str(avg_sentlen))

#calculate average letter count per word
avg_wordlen = lettercount/total_words
print("Average Letter COunt: " + str(avg_wordlen))



