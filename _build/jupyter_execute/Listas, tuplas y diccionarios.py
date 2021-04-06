#!/usr/bin/env python
# coding: utf-8

# # Listas, tuplas y diccionarios

# ## Listas (`list`)
# 
# Las listas son estructuras de datos que pueden almacenar cualquier otro tipo de dato, inclusive una lista 
# puede contener otra lista, además, la cantidad de elementos de una lista se puede modificar removiendo o 
# añadiendo elementos. Para definir una lista se utilizan los corchetes, dentro de estos se colocan todos 
# los elementos separados por comas:

# In[86]:


calificaciones = [10,9,8,7.5,9]
nombres = ["Ana","Juan","Sofía","Pablo","Tania"]
mezcla = [True, 10.5, "abc", [0,1,1]]


# Las listas son *iterables* y por tanto se puede acceder a sus elementos mediante indexación:

# In[87]:


nombres[2]


# In[88]:


nombres[-1]


# Se tiene la posibilidad de agregar elementos a una lista mediante el método `append`: 

# In[89]:


nombres.append("Antonio")
nombres.append("Ximena")
print(nombres)


# El método `remove` elimina un elemento de una lista:

# In[90]:


nombres.remove("Ana")
print(nombres)


# Sí el valor pasado al método `remove` no existe, Python devolverá un `ValueError`:

# In[91]:


nombres.remove("Jorge")


# ### Tuplas (`tuple`)
# 
# Las tuplas son secuencias de elementos similares a las listas, la diferencia principal es que 
# las tuplas no pueden ser modificadas directamente, es decir, una tupla no dispone de los métodos 
# como `append` o `insert` que modifican los elementos de una lista.
# 
# Para definir una tupla, los elementos se separan con comas y se encierran entre paréntesis.

# In[2]:


colores=("Azul","Verde","Rojo","Amarillo","Blanco","Negro","Gris")


# Las tuplas al ser *iterables* pueden accederse mediante la notación de corchetes e índice.

# In[93]:


colores[0]


# In[94]:


colores[-1]


# In[95]:


colores[3]


# Si intentamos modificar alguno de los elementos de la tupla Python nos devolverá un `TypeError`:

# In[96]:


colores[0] = "Café"


# ### Diccionarios (`dict`)

# Los diccionarios son estructuras que contienen una colección de elementos de la 
# forma `clave: valor` separados por comas y encerrados entre llaves. 
# Las claves deben ser objetos inmutables y los valores pueden ser de cualquier tipo. 
# Necesariamente las claves deben ser únicas en cada diccionario, no así 
# los valores. 
# 
# Vamos a definir un diccionario llamado `edades` en el cual 
# cada clave será un nombre y el valor una edad:

# In[3]:


edades = {"Ana": 25, "David": 18, "Lucas": 35, "Ximena": 30, "Ale": 20}


# Puede acceder a cada valor de un diccionario mediante su clave, por ejemplo, 
# si quisieramos obtener la edad de la clave `Lucas` se tendría que escribir:

# In[4]:


edades["Lucas"]

