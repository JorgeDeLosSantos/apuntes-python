#!/usr/bin/env python
# coding: utf-8

# # NumPy: estructuras matriciales
# 
# [NumPy](https://numpy.org/) es una librería de Python que posibilita el trabajar con vectores, matrices y arreglos N-dimensionales de manera eficiente.

# Para el resto del capítulo se asumirá que previo a cualquier código se habrá importado la librería NumPy utilizando el *alias* `np`, como sigue:

# In[14]:


import numpy as np


# ## Definiendo vectores (arreglos unidimensionales)
# 
# Para definir vectores y matrices NumPy dispone de la función `array`, la cual recibe como argumento de entrada una lista de valores y/o una lista que contenga listas anidadas. 
# 
# De manera específica, para definir un arreglo unidimensional (vector), debemos pasar una lista de valores, por ejemplo:

# In[22]:


x = np.array([1,2,3,5,6,7,8,9,10])


# Ese arreglo definido podemos usarlo en operaciones aritméticas y éstas se realizarán elemento a elemento, por ejemplo:

# In[23]:


2*x


# Lo anterior multiplica cada valor contenido en el vector `x` por el valor numérico correspondiente. Algunos otros ejemplos:

# In[24]:


x + 2


# In[25]:


x**2


# Incluso podemos aplicar algunas funciones matemáticas contenidas en NumPy, por ejemplo:

# In[26]:


np.sqrt(x)


# In[27]:


np.sin(x)


# ### La función `linspace`

# La función `linspace` se utiliza para definir un arreglo unidimensional de N-elementos linealmente equiespaciados entre dos valores límites especificados, por ejemplo:

# In[21]:


y = np.linspace(0, 10)
y


# La instrucción anterior crea un vector `y` con 50 valores numéricos entre 0 y 10. Si queremos establecer la cantidad de elementos, debemos introducir un tercer argumento que indique la cantidad de elementos:

# In[13]:


z = np.linspace(0, 10, 11)
z


# El arreglo `z` que resulta contiene 11 elementos entre 0 y 10. 

# ### La función `arange`

# In[31]:


get_ipython().run_line_magic('pinfo', 'np.arange')


# In[ ]:




