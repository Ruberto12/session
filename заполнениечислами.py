#!/usr/bin/env python
# coding: utf-8

# In[21]:


from random import randint
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
lst = [[randint(0, 100) for i in range(b)] for j in range(a)]
print(lst)


# In[ ]:





# In[ ]:




