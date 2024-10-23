#!/usr/bin/env python
# coding: utf-8

# In[11]:



print("My Coffee and Muffin Shop")
num_cof =  input("Number of coffees bought?\n")
num_muf = input("Number of muffins bought?\n")
num_sco =  input("Number of scones bought?\n")
num_tea = input("Number of teas bought?\n")
""" Ask the customer how many of each product they want"""

ttl_cof = float(num_cof)*5.00
ttl_muf = float(num_muf)*4.00
ttl_sco = float(num_sco)*3.00
ttl_tea = float(num_tea)*2.00

print("My Coffee and Muffin Shop Receipt \n" + num_cof +' Coffee at', "$5 each: $", ttl_cof ,"\n" +num_muf, \
      'Muffins at', "$4 each: $", ttl_muf ,"\n" +num_sco, 'Scones at', "$3 each: $", ttl_sco ,"\n" +num_tea, \
      'Teas at', "$2 each: $", ttl_tea)
"""Prints the coffee, muffins, teas, and scones and their respective total prices """
tax = (ttl_muf + ttl_cof)*.06 
"""calulates tax of the total cost of the order"""
print("6% tax: $", tax)

print("Total: $", ttl_muf + ttl_cof + tax)
'''Prints the total of the order'''

print("Thank you for coming to our Coffee Shop. We thank you for spending time and money with us. Enjoy!")



# In[16]:





# In[ ]:




