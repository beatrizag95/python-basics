#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Complete-Python-3-Bootcamp-master/03-Methods and Functions'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Functions and Methods Homework 
# 
# Complete the following questions:
# ____
# **Write a function that computes the volume of a sphere given its radius.**
# <p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>

#%%
def vol(rad):
    return (4/3)*(3.1416)*(rad**3)


#%%
# Check
vol(2)

#%% [markdown]
# ___
# **Write a function that checks whether a number is in a given range (inclusive of high and low)**

#%%
def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} está en el rango entre {} y {}'.format(num,low,high))
    else:
        print('El número no está dentro del rango')


#%%
# Check
ran_check(5,2,7)

#%% [markdown]
# If you only wanted to return a boolean:

#%%
def ran_bool(num,low,high):
    if num in range(low,high+1):
        print('{} está en el rango entre {} y {}'.format(num,low,high))
        return True
    else:
        print('El número no está dentro del rango')
        return False


#%%
ran_bool(3,1,10)

#%% [markdown]
# ____
# **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
# 
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output : 
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
# 
# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
# 
# If you feel ambitious, explore the Collections module to solve this problem!

#%%
def up_low(s):
    d={'upper':0,'lower':0}
    for c in s:
      if c.isupper():
        d['upper']+=1
      elif c.islower():
        d['lower']+=1
    print('Original String: ', s)
    print('No. of lower: ', d['lower'])
    print('No. of upper: ', d['upper'])

#%%
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#%% [markdown]
# ____
# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
# 
#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]

#%%
def unique_list(lst):
    return list(set(lst))

#%%
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

#%% [markdown]
# ____
# **Write a Python function to multiply all the numbers in a list.**
# 
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24

#%%
def multiply(numbers):  
    total=1
    for perro in numbers:
      total *= perro
    return total


#%%
multiply([1,2,3,-4])

#%% [markdown]
# ____
# **Write a Python function that checks whether a passed in string is palindrome or not.**
# 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

#%%
def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]


#%%
palindrome('helleh')

#%% [markdown]
# ____
# #### Hard:
# 
# **Write a Python function to check whether a string is pangram or not.**
# 
#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"
# 
# Hint: Look at the string module

#%%
#ojo
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


#%%
ispangram("The quick brown fox jumps over the lazy dog")


#%%
string.ascii_lowercase

#%% [markdown]
# #### Great Job!

