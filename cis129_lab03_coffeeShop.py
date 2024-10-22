#!/usr/bin/env python
# coding: utf-8

# In[11]:



print("My Coffee and Muffin Shop")
num_cof =  input("Number of coffees bought?\n")
num_muf = input("Number of muffins bought?\n")
""" Ask the customer how many of each product they want"""

ttl_cof = float(num_cof)*5.00
ttl_muf = float(num_muf)*4.00
print("My Coffee and Muffin Shop Receipt \n" + num_cof +' Coffee at', "$5 each: $", ttl_cof ,"\n" +num_cof,      'Muffins at', "$4 each: $", ttl_muf)
"""Prints the coffee, muffin  and their respective total prices """
tax = (ttl_muf + ttl_cof)*.06 
"""calulates tax of the total cost of the order"""
print("6% tax: $", tax)

print("Total: $", ttl_muf + ttl_cof + tax)
'''Prints the total of the order'''


# In[16]:





# In[ ]:




