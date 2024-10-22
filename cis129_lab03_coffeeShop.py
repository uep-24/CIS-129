#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = b = 7
print('a =', a, '\nb =', b)
There is nothing wrong with this code


# In[7]:


print('Enter two integers, and I will tell you', 'the relationships they satisfy.')
# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))
if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print(number1, 'is not equal to', number2)
          
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
else:
    print(number1, 'is greater than', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)
else:
    print(number1, 'is less than', number2)


# In[4]:


'What is your problem?' When the user answers and presses Enter, the script should simply ignore the user’s input, 
   then prompt the user again with 'Have you had this problem before (yes or no)?' If the user enters 'yes', print 
   'Well, you have it again.'
   If the user answers 'no', print 'Well, you have it now.'

get_ipython().set_next_input('Would this conversation convince the user that the entity at the other end exhibited intelligent behavior? Why or why not');get_ipython().run_line_magic('pinfo', 'not')


# In[9]:


option1 = input('What is your problem? ')

option2= input('Have you had this problem before (yes or no)? ')

if option2 == 'yes':
    print('Well, you have it again.')
elif option2 == 'no':
    print('Well, you have it now.')
    
This conversation wuld not convince the user that the entity at the other end exhibited intelligent behavior. 
Because there is a clear possibility that the user enters "I don't remember" instead of "no" or another string and the 
program won't return anything


# In[ ]:




