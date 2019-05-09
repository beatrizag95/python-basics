#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Complete-Python-3-Bootcamp-master/03-Methods and Functions'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Function Practice Exercises
# 
# Problems are arranged in increasing difficulty:
# * Warmup - these can be solved using basic comparisons and methods
# * Level 1 - these may involve if/then conditional statements and simple methods
# * Level 2 - these may require iterating over sequences, usually with some kind of loop
# * Challenging - these will take some creativity to solve
#%% [markdown]
# ## WARMUP SECTION:
#%% [markdown]
# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

#%%
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)


#%%
# Check
lesser_of_two_evens(2,4)


#%%
# Check
lesser_of_two_evens(2,5)

#%% [markdown]
# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

#%%
def animal_crackers(text):
    words = text.split(' ')
    
    if words[0][0] == words[1][0]:
        return True 
    else:
        return False


#%%
# Check
animal_crackers('Levelheaded Llama')


#%%
# Check
animal_crackers('Crazy Kangaroo')

#%% [markdown]
# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

#%%
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        return True
    else:
        return False


#%%
# Check
makes_twenty(20,10)


#%%
# Check
makes_twenty(2,3)

#%% [markdown]
# # LEVEL 1 PROBLEMS
#%% [markdown]
# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#      
#     old_macdonald('macdonald') --> MacDonald
#     
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

#%%
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
    #otra forma
    #newname = ''
    #index=0
    #for letter in name:
    #   if index == 0 or index == 3:
    #        newname = newname+letter.upper()
    #    else:
    #        newname = newname+letter
    #    index=index+1
    #return newname


#%%
# Check
old_macdonald('macdonald')

#%% [markdown]
# ###### MASTER YODA: Given a sentence, return a sentence with the words reversed
# 
#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'
#     
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# 
#     >>> "--".join(['a','b','c'])
#     >>> 'a--b--c'
# 
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# 
#     >>> " ".join(['Hello','world'])
#     >>> "Hello world"

#%%
def master_yoda(text):
    text1 = text.split(' ')
    text2 = reversed(text1)
    text3 = ' '.join(text2)
    print(text3)


#%%
# Check
master_yoda('I am home')


#%%
# Check
master_yoda('We are ready')

#%% [markdown]
# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

#%%
def almost_there(n):
    if n in range(90,111):
      return True
    elif n in range(190,211):
      return True
    else:
      return False
      


#%%
# Check
almost_there(104)


#%%
# Check
almost_there(150)


#%%
# Check
almost_there(209)

#%% [markdown]
# # LEVEL 2 PROBLEMS
#%% [markdown]
# #### FIND 33: 
# 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# 
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

#%%
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        if nums[i] == 3 and nums[i+1] == 3:
        #if nums[i:i+2] == [3,3]:
            return True  
    
    return False

#%%
# Check
has_33([1, 3, 3])


#%%
# Check
has_33([1, 3, 1, 3])


#%%
# Check
has_33([3, 1, 3])

#%% [markdown]
# #### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     paper_doll('Hello') --> 'HHHeeellllllooo'
#     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

#%%
def paper_doll(text):
    text2 = [x+x+x for x in text]
    return ''.join(text2)


#%%
# Check
paper_doll('Hello')


#%%
# Check
paper_doll('Mississippi')

#%% [markdown]
# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

#%%
def blackjack(a,b,c):
    if (a+b+c) <= 21:
      return (a+b+c)
    elif (a+b+c) > 21 and (a==11 or b==11 or c==11):
      return (a+b+c)-10
    elif (a+b+c) > 21:
      return 'BUST'


#%%
# Check
blackjack(5,6,7)


#%%
# Check
blackjack(9,9,9)


#%%
# Check
blackjack(9,9,11)

#%% [markdown]
# #### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#  
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14

#%%
#solución
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
#%%
# Check
summer_69([1, 3, 5])


#%%
# Check
summer_69([4, 5, 6, 7, 8, 9])


#%%
# Check
summer_69([2, 1, 6, 9, 11])

#%% [markdown]
# # CHALLENGING PROBLEMS
#%% [markdown]
# #### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# 
#      spy_game([1,2,4,0,0,7,5]) --> True
#      spy_game([1,0,2,4,0,5,7]) --> True
#      spy_game([1,7,2,0,4,5,0]) --> False
# 

#%%
#solution
def spy_game(nums):
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
       
    return len(code) == 1


#%%
# Check
spy_game([1,2,4,0,0,7,5])


#%%
# Check
spy_game([1,0,2,4,0,5,7])


#%%
# Check
spy_game([1,7,2,0,4,5,0])

#%% [markdown]
# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25
# 
# By convention, 0 and 1 are not prime.

#%%
#solution
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3,x,2): 
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
                


#%%
# Check
count_primes(100)

#%% [markdown]
# ### Just for fun:
# #### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#     print_big('a')
#     
#     out:   *  
#           * *
#          *****
#          *   *
#          *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. <br>For purposes of this exercise, it's ok if your dictionary stops at "E".

#%%
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*****',4:'*   *',5:'***  ',6:'*  * ',7:'**   ',8:'*    ',9:'**** '}
    alphabet = {'A':[1,2,3,4,4], 'B':[5,6,7,6,5], 'C':[3,8,8,8,3], 'D':[5,6,4,6,5], 'E':[3,8,9,8,3]}
    for pattern in alphabet[letter.upper()]:
      print(patterns[pattern])

#%%
print_big('e')

#%% [markdown]
# ## Great Job!