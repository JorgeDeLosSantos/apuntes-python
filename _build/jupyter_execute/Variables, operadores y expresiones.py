#!/usr/bin/env python
# coding: utf-8

# # Variables, operadores y expresiones
# 
# Al ser un lenguaje de alto nivel, Python dispone de los tipos de datos elementales en cualquier lenguaje de programación, 
# pero además incluye estructuras de datos más complejas y con altas prestaciones que facilitan en muchos 
# aspectos la tarea del programador.
# 
# Python es un lenguaje de tipado dinámico en el que no hace falta declarar el tipo de dato que asignará a una variable, 
# de igual manera una variable puede cambiar de tipo conforme la ejecución del programa, por ello se debe tener cuidado 
# con la sintaxis para definir cada tipo de dato.

# ## Variables
# 
# En Python todo lo que creamos son objetos y las variables son referencias a esos objetos, las variables se definen por asignación utilizando el signo `=`, por ejemplo:

# In[7]:


a = 5
b = 8.0
nombre = "Catalina"


# Piensa el proceso de asignación como la acción de etiquetar las direcciones de memorias en donde se almacenan los objetos de Python, tal como se esquematiza en la figura.
# 
# <img src="../img/variables/variables_1.svg">

# Veamos ahora otro ejemplo de definición de variables:

# In[9]:


m = 7
n = m


# En este caso primero definimos la variable `m` que será una *etiqueta* del objeto `7`, cuando se hace la asignación `n = m` se *coloca otra etiqueta* al objeto `7`.
# 
# <img src="../img/variables/variables_2.svg">

# Se puede verificar que ambas variables refieren al mismo objeto:

# In[11]:


print( id(m) )
print( id(n) )


# La función `id` devuelve el identificador del objeto, cada identificador es único durante el ciclo de vida de cada objeto.

# El nombre de una variable puede constar de una combinación de caracteres alfanúmericos y el guión bajo, 
# siempre y cuando el primer caracter no sea un dígito. Además, en Python los nombres de variables son 
# *case sensitive*, es decir, se distingue entre mayúsculas y minúsculas.

# In[12]:


D = 177.8
d = 95


# In[2]:


print(D)


# In[3]:


print(d)


# Existen algunas palabras reservadas del lenguaje que no puede utilizar como nombre de variable, 
# puede verificar cuáles son estas palabras tecleando lo siguiente:

# In[4]:


import keyword 
print(keyword.kwlist)


# ## Tipos de datos básicos

# ### Enteros (`int`)
# 
# Los enteros son un tipo de dato básico en cualquier lenguaje de programación. En Python para definir un valor entero se debe colocar el número sin ningun punto decimal, por ejemplo:

# In[5]:


a = 1
type(a)


# De manera explícita se puede definir un valor entero utilizando la función `int`:

# In[6]:


m = 5.0
n = int(5.0)
type(m), type(n)


# Observe que cuando colocamos un punto decimal, automáticamente la cantidad deja de ser un entero y pasa a ser un flotante.

# ### De coma flotante (`float`)
# 
# Los valores de coma flotante son cantidades numéricas que incluyen a todos los reales. Para que Python reconozca un valor numérico como de tipo `float` se debe adicionar el punto decimal o bien utilizar la función `float` para hacer la indicación de manera explícita, por ejemplo:

# In[7]:


w = 5.3
x = 10.0
y = 9.
z = float(8)
type(w), type(x), type(y), type(z)


# ### Booleanos (`bool`)
# 
# Las variables booleanas sólo pueden adoptar dos valores: verdadero (`True`) o falso (`False`). Un valor booleano se puede definir directamente a partir de las constantes `True` y `False`:

# In[8]:


a = True
b = False
type(a), type(b)


# O bien a partir de otros objetos Python al aplicar la función `bool`:

# In[9]:


bool("hola")


# In[10]:


bool([])


# In[11]:


bool(0)


# In[12]:


bool(10)


# En general, la función `bool` devolverá un `False` cuando se tienen objetos nulos o vacíos, en cualquier otro caso devolverá el valor `True`.

# ## Operadores relacionales y lógicos
# 
# Los operadores relacionales (o de comparación) nos permite efectuar comparaciones entre objetos de Python. El resultado de una comparación es un valor booleano `True` o `False`, dependiendo la naturaleza de la comparación.
# 
# A continuación se ejemplifican los operadores relacionales que podemos utilizar en Python:

# In[5]:


# "igual a"
1 == 1


# In[6]:


# "diferente a"
"a" != "a"


# In[7]:


# mayor que
10 > 5


# In[8]:


# menor que
5 < 1


# In[9]:


# mayor o igual que
30 >= 30


# In[10]:


# menor o igual que
20 <= 10


# Hay que tener cuidado y verificar que al hacer comparaciones los objetos implicados sean compatibles. Cuando los objetos no son comparables Python devolverá un `TypeError`, por ejemplo:

# In[11]:


"a" > 10


# In[ ]:


[0,4] < (1,2)


# También podemos *encadenar* comparaciones con instrucciones del tipo `a < b < c`, donde ese `<` puede ser cualquier operador relacional, por ejemplo:

# In[12]:


1 < 2 < 3


# In[13]:


10 > 10 > 3


# In[14]:


3 == 3 >= 2


# Los **operadores lógicos** nos sirven para realizar operaciones de lógica booleana entre valores de tipo `bool`. En Python podemos utilizar los operadores lógicos `and`, `or` y `not`, observe los siguientes ejemplos:

# In[15]:


True and True


# In[16]:


True and False


# In[17]:


True or False


# In[121]:


not True


# In[122]:


(1 == 1) and (2 > 1)


# In[123]:


(0 == 0) or (10 >=20) and (1 > 0)


# In[124]:


not( (2 > 3) and (5==5) )

