# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 06:08:47 2021

@author: v-kgordon
"""

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
