#!/usr/bin/env python
# coding: utf-8

# # Cadenas de caracteres
# 
# Las cadenas de caracteres (denominadas habitualmente y de manera indistinta como *strings* es un tipo de dato 
# que contiene una secuencia de símbolos, mismos que pueden ser alfanúmericos hasta cualquier otro símbolo propio de 
# un sistema de escritura. En Python los strings se definen entre comillas dobles o simples:

# In[78]:


"esta es una cadena de caracteres"


# In[79]:


'esta también'


# Puede concatenar dos strings utilizando el operador `+`:

# In[80]:


"Hola" + "mundo"


# Notará que Python por sí mismo no sabe que estamos uniendo dos palabras y que entre ellas debería haber un espacio 
# para su correcta lectura, evidentemente este tipo de cuestiones son las que el programador debe tomar en cuenta al 
# escribir un código.
# 
# Una cadena de caracteres es lo que en Python se conoce como *iterable*, es decir, una secuencia de 
# elementos agrupados a los cuales se puede acceder de manera individual mediante indexación. Por ejemplo, 
# sea `nombre` una cadena de caracteres dada por:

# In[81]:


nombre="Catalina"


# Puede acceder a cada una de las letras que componen dicha cadena mediante la notación `iter[pos]`, donde 
# `iter` es el nombre del iterable y `pos` la posición en que se encuentra el caracter al cual 
# se desea acceder, siendo 0 para la primera letra, 1 para la segunda y así de manera consecutiva. Por ejemplo: 

# In[82]:


nombre[0]


# In[83]:


nombre[4]


# In[84]:


nombre[2]


# Al último elemento, sin importar la longitud de la cadena, se accede con el índice -1:

# In[85]:


nombre[-1]

