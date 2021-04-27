# PalindromeProject

This project is using Palindromes to show list manipulation, run time foundations, and introducing sets and time functions. 

After creating a file for the word list, you then want to be able to reference it. In the case that the file does not exist, I used a try/except function
so that my program will do a system exit. 
```
import sys

def load(file):
    # Open a text file and return a list of lower case strings
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1) 
```

You then create a function that finds whether or not a word is a Palindrome by taking the word and comparing it to the word reversed.
If the two equal one another, then that word is the same spelled regularly as it is spelled in reverse and thus meets the definition for Palindrome.
```
pali_list = []

for word in word_list:     
    #1st colon START : END (Index of the word) 2nd Colon (After end and how you go through the word) so -1 reverses the word 
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
```

This code is great for single words, but there are also two words that can be a Palindrome so we want to check our word list for these as well. 
EX: TACO CAT == TAC OCAT (Without spaces)

```
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
```
I then wanted to see the run time of this file so I used a cProfile function. 
```
import cProfile
import Pallindromes
cProfile.run('Pallindromes.find_palingrams()')
```
Afterward, I could simply get the exact runtime from start to finish without all the metrics by importing time and running throughout the entirity of the program.
```
import time
start_time = time.time()
end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))
```
My first result was "Runtime for this program was 43.90109944343567 seconds."
This wasn't too bad, but waiting 43 seconds for Palidromes is unacceptable. I would like to know my Palindromes near immediately! 
Knowing I could do better, I setup my Palindromes using sets instead of lists. Since sets are built to store multiple variables into 
a single variable, the program can run much more effeciently. 
```
Runtime for this program was 0.04596567153930664 seconds
```
Much. MUCH better. Since this program is running through about 62,000 entries, I was ready to move onto to my next project. I gave my laptop a little tap on the keyboard and git pushed the program to completion. 

This program can also be solved Recursively!

```
import load_Dictionary
word_list = load_Dictionary.load('2of4brif.txt')

def find_palindromes(word, start_index, end_index):
    #base case (When we are going to stop calling the function)
    if start_index == end_index:
        return True
    if word[start_index] == word[end_index]:
        return find_palindromes(word, start_index + 1, end_index - 1)
    else: 
        return False

pali_list = []
for i in word_list:
    if len(i) > 0: 
    #We need to store the upper version of i into i (Case sensitive)
        i = i.upper()
    #Need to store the return value of find_palindromes
        start = find_palindromes(i, 0, len(i)-1) 
        if start == True:
            pali_list.append(i)

for palindrome in pali_list :
    print(palindrome)
    ```
And here is a full walkthrough on how this program works:

```
 # MADAM
    #First function call
    #To represent last letter of string: Len(word) -1
    #find_palindromes("MADAM", 0, 4)
        #(1st if) Does start_index == end_index? 0 == 4? NO
        #(2nd if) Does word[start_index] == word[end_index]? Does 'M' == 'M'? YES
            #(Now go inside the if) Call the function again, 
            #find_palindromes('MADAM', 1, 3) 
            #Does 1 = 3? NO
            #Does 'A' == 'A'? YES
                #find_palindromes ('MADAM', 2, 2)
                # Does 2 = 2? YES
                    #Returns True and ends. 
    
    # NOUN
    #find_palindromes ('NOUN', 0, 3)
        #1st if - Does 0 == 3? NO
        #2nd if - Does 'N' == 'N'? YES
            #find_palindromes ('NOUN', 1, 2)
                #1st if - Does 1 == 2? NO
                #2nd if- Does 'O' == 'U'? NO
                #else - return false and end. 
```
