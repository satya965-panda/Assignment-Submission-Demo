#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum = 0

while True:
  number = int(input("Enter the number :"))
  sum += number
  

  choice = input("Want to sum another number ? (y/n) :")
  if choice.casefold() == 'n':
      break;

print(f"sum : {sum}")


# In[ ]:




