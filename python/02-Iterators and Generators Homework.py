#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'jupyter'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Iterators and Generators Homework 
# 
# ### Problem 1
# 
# Create a generator that generates the squares of numbers up to some number N.

#%%
def gensquares(N):
    for i in range(N):
        yield i**2


#%%
for x in gensquares(10):
    print(x)

#%% [markdown]
# ### Problem 2
# 
# Create a generator that yields "n" random numbers between a low and high number (that are inputs). <br>Note: Use the random library. For example:

#%%
import random

random.randint(1,10)


#%%
def rand_num(low,high,n):
    
    for i in range(n):
        yield random.randint(low, high)


#%%
for num in rand_num(1,10,12):
    print(num)

#%% [markdown]
# ### Problem 3
# 
# Use the iter() function to convert the string below into an iterator:
# 

#%%
s = 'hello'

s = iter(s)

print(next(s))

#%% [markdown]
# 
#%% [markdown]
# ### Extra Credit!
# Can you explain what *gencomp* is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

#%%
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

#%% [markdown]
# Hint: Google *generator comprehension*!
# 
# # Great Job!

