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
# ![](img/variables/variables_1.svg)

# Veamos ahora otro ejemplo de definición de variables:

# In[13]:


m = 7
n = m


# En este caso primero definimos la variable `m` que será una *etiqueta* del objeto `7`, cuando se hace la asignación `n = m` se *coloca otra etiqueta* al objeto `7`.
# 
# ![](img/variables/variables_2.svg)

# Se puede verificar que ambas variables refieren al mismo objeto:

# In[14]:


print( id(m) )
print( id(n) )


# La función `id` devuelve el identificador del objeto, cada identificador es único durante el ciclo de vida de cada objeto.

# Para nombrar las variables se deben tener en cuenta las consideraciones que a continuación se describen.

# * Los nombres de variables sólo deben contener letras, números y guiones bajos.

# In[19]:


esfuerzo_axial = 150e6
diametro_01 = 30e-3
nombre = "Ximena"


# * El nombre de una variable puede comenzar con una letra o un guión bajo, pero no con un número
# 
# Los siguientes nombres de variables son válidos:

# In[21]:


temperatura = 35
_deformacion_unitaria = 300e-6


# Pero este no, puesto que comienza con un número:

# In[22]:


30_presion = 30e3


# * Los espacios no están permitidos en los nombres de variables. Sí necesitas nombrar una variable con dos o más palabras, puedes utilizar el guión bajo para separar las palabras.

# In[23]:


modulo de elasticidad = 70e9


# In[24]:


modulo_de_elasticidad = 70e9


# * Evita utilizar palabras claves/reservadas y nombres de funciones y/o cualquier otra palabra que Python utilice.
# 
# Por ejemplo, observa que pasa si intentamos utilizar como nombre de variable la palabra reservada `lambda`:

# In[25]:


lambda = 1500


# Python nos manda un `SyntaxError`. La lista de palabras reservadas del lenguaje que no puedes utilizar como nombre de variable la puedes listar con las siguientes instrucciones:

# In[26]:


import keyword 
print(keyword.kwlist)


# Ademas de las palabras reservadas del lenguaje, evita utilizar los nombres de funciones o clases *built-in* de Python, esos nombres los puedes ver tecleando las siguientes instrucciones:

# In[28]:


import builtins
print( dir(builtins) )


# * Los nombres de variables son *case sensitive*, es decir, se distingue entre mayúsculas y minúsculas.
# 
# No es lo mismo definir una variable `nombre` que otra llamada `NOMBRE`:

# In[30]:


NOMBRE = "Ana"
nombre = "Paola"
nombre == NOMBRE


# * Los nombres de variables deberían ser cortos pero descriptivos. 
# 
# Por ejemplo, si estamos *almacenando* un valor que corresponde a un diámetro, suele ser más conveniente y recomendable utilizar `diametro` en lugar de `d` como nombre de variable.
# 
# 
# Puedes encontrar más recomendaciones sobre cómo nombrar variables en la [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

# ## Tipos de datos básicos

# ### Enteros (`int`)
# 
# Los enteros son un tipo de dato básico en cualquier lenguaje de programación. En Python para definir un valor entero se debe colocar el número sin ningun punto decimal, por ejemplo:

# In[33]:


a = 1
type(a)


# En el código anterior la función `type` nos sirve para identificar la clase/tipo de un objeto.

# De manera explícita se puede definir un valor entero utilizando la función `int`:

# In[36]:


m = 5.0
n = int(5.0)
type(m), type(n)


# Observa que cuando colocamos un punto decimal, automáticamente la cantidad deja de ser un entero y pasa a ser un flotante.

# ### De coma flotante (`float`)
# 
# Los valores de coma flotante son cantidades numéricas que incluyen a *todos los reales*. Para que Python reconozca un valor numérico como de tipo `float` se debe adicionar el punto decimal o bien utilizar la función `float` para hacer la indicación de manera explícita, por ejemplo:

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

# Usualmente los valores booleanos siempre van a provenir de una comparación entre objetos, para efectuar esas comparaciones se utilizan los operadores relacionales.

# ## Operadores aritméticos

# ### Operador suma (`+`)

# In[57]:


1000 + 2000


# ### Operador resta (`-`)

# In[58]:


500 - 350


# ### Operador multiplicación (`*`)

# In[59]:


352 * 34


# ### Operador división (`/`)

# In[60]:


3/8


# ### Operador de potenciación (`**`)

# In[62]:


10**3


# ### Operador módulo 

# In[66]:


250 % 100


# ### Operador división entera

# In[68]:


50 // 6


# ## Operadores relacionales
# 
# Los operadores relacionales (o de comparación) nos permite efectuar comparaciones entre objetos de Python. El resultado de una comparación es un valor booleano `True` o `False`. A continuación se ejemplifican los operadores relacionales que podemos utilizar en Python:

# In[39]:


# "igual que"
1 == 1


# In[40]:


# "diferente a"
"a" != "a"


# In[41]:


# mayor que
10 > 5


# In[42]:


# menor que
5 < 1


# In[43]:


# mayor o igual que
30 >= 30


# In[44]:


# menor o igual que
20 <= 10


# Hay que tener cuidado y verificar que al hacer comparaciones los objetos implicados sean compatibles. Cuando los objetos no son comparables Python devolverá un `TypeError`, por ejemplo:

# In[45]:


"a" > 10


# In[46]:


[0,4] < (1,2)


# También podemos *encadenar* comparaciones con instrucciones del tipo `a < b < c`, donde ese `<` puede ser cualquier operador relacional, por ejemplo:

# In[47]:


1 < 2 < 3


# In[48]:


10 > 10 > 3


# In[49]:


3 == 3 >= 2


# ## Operadores lógicos
# 
# Los **operadores lógicos** nos sirven para realizar operaciones de lógica booleana entre valores de tipo `bool`. En Python podemos utilizar los operadores lógicos `and`, `or` y `not`, observe los siguientes ejemplos:

# In[50]:


True and True


# In[51]:


True and False


# In[52]:


True or False


# In[53]:


not True


# In[54]:


(1 == 1) and (2 > 1)


# In[55]:


(0 == 0) or (10 >=20) and (1 > 0)


# In[56]:


not( (2 > 3) and (5==5) )


# ## Ejercicios

# In[ ]:




