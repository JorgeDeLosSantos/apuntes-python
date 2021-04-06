#!/usr/bin/env python
# coding: utf-8

# # NumPy: estructuras matriciales
# 
# [NumPy](https://numpy.org/) es una librería de Python que posibilita el trabajar con vectores, matrices y arreglos N-dimensionales de manera eficiente.

# Para el resto del capítulo se asumirá que previo a cualquier código se habrá importado la librería NumPy utilizando el *alias* `np`, como sigue:

# In[22]:


import numpy as np


# ## El `array` de NumPy

# In[ ]:





# ## Vectores (arreglos unidimensionales)
# 
# Para definir vectores y matrices NumPy dispone de la función `array`, la cual recibe como argumento de entrada una lista de valores y/o una lista que contenga listas anidadas. 
# 
# De manera específica, para definir un arreglo unidimensional (vector), debemos pasar una lista de valores, por ejemplo:

# In[23]:


x = np.array([1,2,3,5,6,7,8,9,10])


# Ese arreglo definido podemos usarlo en operaciones aritméticas y éstas se realizarán elemento a elemento, por ejemplo:

# In[24]:


2*x


# Lo anterior multiplica cada valor contenido en el vector `x` por el valor numérico correspondiente. Algunos otros ejemplos:

# In[25]:


x + 2


# In[26]:


x**2


# Incluso podemos aplicar algunas funciones matemáticas contenidas en NumPy, por ejemplo:

# In[27]:


np.sqrt(x)


# In[28]:


np.sin(x)


# ### La función `linspace`

# La función `linspace` se utiliza para definir un arreglo unidimensional de N-elementos linealmente equiespaciados entre dos valores límites especificados, por ejemplo:

# In[29]:


y = np.linspace(0, 10)
y


# La instrucción anterior crea un vector `y` con 50 valores numéricos entre 0 y 10. Si queremos establecer la cantidad de elementos, debemos introducir un tercer argumento que indique la cantidad de elementos:

# In[30]:


z = np.linspace(0, 10, 11)
z


# El arreglo `z` que resulta contiene 11 elementos entre 0 y 10. 

# ### La función `arange`

# In[ ]:





# ## Matrices

# ### Operaciones básicas

# In[31]:


A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A,B, sep="\n\n")


# In[32]:


A + B # suma


# In[33]:


A - B # resta


# In[34]:


A @ B # multiplicación matricial


# In[35]:


B @ A # multiplicación matricial


# ### Inversa y determinante

# In[36]:


from numpy.linalg import inv, det


# In[37]:


inv(A)


# In[38]:


inv(B)


# In[39]:


inv(A) @ A


# In[40]:


# np.set_printoptions(suppress=True)


# In[41]:


inv(A) @ A


# In[42]:


det(B)


# In[ ]:





# In[ ]:




