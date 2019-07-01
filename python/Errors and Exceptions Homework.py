#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'jupyter'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Errors and Exceptions Homework
#%% [markdown]
# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

#%%
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")

#%% [markdown]
# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

#%%
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')

#%% [markdown]
# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

#%%
def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)


#%%
ask()

#%% [markdown]
# # Great Job!

