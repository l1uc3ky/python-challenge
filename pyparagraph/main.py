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

# #define sentences 
sentences = patxt.split('.')

# #Loop through sentences to count words
# for sentence in sentences: 
#     words = sentence.split(' ')
#     wordcounts.append(len(words))




# # import re
# # re.split("(?&lt;=[.!?]) +", paragraph)
