# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 05:01:53 2021

@author: v-kgordon
"""

#This is the most Optimized version of the Palindrome
#This code uses sets instead of lists
import time
start_time = time.time()
import load_Dictionary
word_list = load_Dictionary.load('2of4brif.txt')


def find_palingrams():
#Find dictionary palingrams.
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:]in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:]and rev_word[:end-i]in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))

"""
#This is for Palindrome phrases
import time
start_time = time.time()
import load_Dictionary
word_list = load_Dictionary.load('2of4brif.txt')
#finding word pair palindromes in a dictionary file

def find_palingrams():
    #Find dictionary palingrams
    pali_list = []
    for word in word_list:
        length = len(word)
        reversed_word = word[::-1]
        if length > 1:
            for i in range(length):
                #[i:] start at the beginning index all the way to the end. 
                if word[i:] == reversed_word[:length-i] and reversed_word[length-i:] in word_list:
                    pali_list.append((word, reversed_word[length-i:]))
                if word[:i] == reversed_word[:length-i] and reversed_word[:length-i] in word_list:
                    pali_list.append((reversed_word[:length-i], word))
    return pali_list

palingrams = find_palingrams()
#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of Palingrams = {}\n".format(len(palingrams_sorted))) 

for first, second in palingrams_sorted:
    print("{}{}".format(first, second))

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))
"""





""" THIS IS HOW YOU FIND SINGLE WORD PALINDROMES 
pali_list = []

for word in word_list:     
    # 1st colon START : END (Index of the word) 2nd Colon (After end and how you go through the word) so -1 reverses 
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
"""


            