#!/usr/bin/env python
# coding: utf-8

# # Funciones
# 
# Las funciones son *porciones de código* que nos sirven para modularizar 
# nuestros programas y evitar en muchos casos la repetitividad de código. 
# De manera general una función recibe algunos valores de entrada, los *procesa* y 
# devuelve algunos valores de salida (o bien modifica algunas variables).
# 
# ## Funciones *built-in*
# 
# Python dispone de algunas funciones nativas que se *cargan* automáticamente cuando se 
# inicia el intérprete. Por ejemplo la función `max` devuelve el mayor valor numérico de 
# una lista de números:

# In[151]:


max([10,35,5,110,48,30,112,98,87])


# También existe una función `min`, análoga a `max`:

# In[152]:


min([10,35,5,110,48,30,112,98,87])


# Otro ejemplo de función nativa es `bin`, la cual dado un número en base 10 devuelve 
# una cadena con la representación en base 2.

# In[153]:


bin(10)


# Naturalmente, el valor devuelto por una función se puede asignar a una variable y posteriormente ser utilizado:

# In[154]:


a = max([10,5,8])
b = min([10,5,8])
h = (a - b)/10
print(h)


# Hay funciones que no devuelven como tal un valor, si no que pueden modificar directamente 
# alguna variable global o simplemente mostrar algo en la salida estándar como el caso de `print`.
# 
# Tendremos también funciones que aceptan más de un argumento, por ejemplo a la función `round` podemos 
# pasarle dos argumentos: un número real y la cantidad de lugares decimales a considerar para el redondeo.
# 

# In[155]:


round(3.141592653589793, 6)


# In[156]:


round(3.141592653589793, 2)


# ### La función `print`
# 
# La función `print` se utiliza para mostrar en pantalla el *valor* (o la representación) de los objetos Python. A `print` le podemos pasar un sólo argumento, por ejemplo:

# In[1]:


print("Hola mundo")


# O una lista de argumentos que se imprimirán:

# In[2]:


print("hola", "mundo", 5, 8, [1,2,3])


# Como se puede observar en la línea anterior, realmente, le podemos pasar cualquier objeto de Python y `print` nos devolverá la representación de dicho objeto. 
# 
# Adicionalmente, también podemos indicar de manera explícita, mediante el *keyword argument* `sep`, el separador que queremos utilizar, por default el separador es un espacio.

# In[3]:


print(20,30,"python", sep=",")


# In[4]:


print("Hola", 90, 80, sep=" -- ")


# Como separador podemos utilizar cualquier símbolo soportado por Python.

# In[5]:


print("Hola", 90, 80, sep=" \u21e8 ")


# In[6]:


print("Hola", "mundo", sep=" \U0001F600 ")


# Se puede indicar, también, mediante el *keyword argument* `end`, el caracter que se quiere utilizar cuando se *imprime* el último elemento, por default es un salto de línea.

# In[7]:


print(20,30,"python") # sin cambiar el argumento end 
print("hola")


# Cambiando el argumento `end`:

# In[8]:


print(20,30,"python", end="\n\n\t") # utilizando un doble salto de línea + tab
print("hola")


# ```{admonition} print y los strings formateados
# :class: tip
# Si te interesa obtener información acerca de `print` y su uso conjunto con strings formateados, revisa el capítulo dedicado a los strings.
# ```

# ### La función `input`

# En Python, la función `input` permite obtener entrada por teclado, con la finalidad de *tomar* información proporcionada por el usuario. La sintaxis de `input` es:
# 
# ```python
# var = input(prompt)
# ```
# 
# Donde `prompt` es el mensaje que se muestra al usuario al momento que se le solicita la información, `var` es la variable en la cual se almacena lo que el usuario ingresa hasta que presiona la tecla **Enter**.
# 
# Veamos un ejemplo:

# In[9]:


nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "bienvenido")


# Como puedes observar, el programa anterior solicita al usuario un valor de entrada utilizando el prompt `Ingrese su nombre: `; en este caso el usuario ingresó la cadena `Jorge`. Con la segunda línea únicamente se toma el valor guardado en la variable nombre y se muestra junto con  las cadenas `"Hola"` y `"bienvenido"`.

# Es importante tener en cuenta que la función `input` devuelve siempre un valor de tipo string. Así, si quisiéramos solicitar un valor de tipo numérico y realizar operaciones con él, entonces, se debe tener el cuidado de convertir el string a un tipo numérico de manera explícita, de lo contrario podríamos tener un programa que nos *lance* un error, o en el peor de los casos, que funcione de manera incorrecta.

# In[20]:


# No podemos sumar un string con un entero
n = input("Ingrese un número: ")
print(n + 10)


# In[19]:


# Aquí n+n+n corresponde a concatenar la cadena "12", en lugar de sumar los valores numéricos.
n = input("Ingrese un número: ")
print(n + n + n)


# In[13]:


# Ahora n+n+n si corresponde a sumar dichos valores numéricamente
n = float( input("Ingrese un número: ") )
print(n + n + n)


# ## Funciones definidas por el usuario

# Además de las funciones nativas de Python, es posible definir nuestras propias funciones. En Python, de manera general, una función se define siguiendo la estructura mostrada a continuación:
# 
# ```python
# def nombre_fun(arg1, arg2, ..., argN):
#     # Cuerpo de la función
#     # .
#     # .
#     # .
#     return val1, val2, ..., valN
# ```
# 
# Donde `def` es una palabra que debe anteceder siempre a la definición de una función, 
# `nombre_fun` es el nombre que se asignará a la función, entre paréntesis y 
# separados por comas se colocan los nombres de los argumentos de entrada, los dos puntos 
# se colocan después de cerrar el paréntesis e indican que ahí termina el *encabezado* de 
# la función y comenzará el *cuerpo* de la misma, aquí se colocarán todas las 
# instrucciones que deberán realizarse; la palabra reservada `return` sirve para 
# indicar los valores a devolver, mismos que se colocarán separados por comas.
# 
# Vamos a definir una función llamada `saluda`, la cual recibe un nombre (string)
# y devuelve un saludo (string) formado mediante concatenación:
# 

# In[10]:


def saluda(nombre):
    s = "Hola " + nombre + ", bienvenido."
    return s


# In[11]:


print(saluda("Jorge"))


# Lo único que hace la función anterior es tomar un *string* como argumento y unirlo 
# a algunas cadenas ya establecidas dentro de la función. 
# 
# Veamos ahora cómo definir una función que recibe como argumento un entero y devuelve un valor lógico que 
# indica si este es par.

# In[159]:


def espar(n):
    if n%2 == 0:
        s = True
    else:
        s = False
    return s


# In[160]:


print(espar(2))
print(espar(5))
print(espar(10))


# Naturalmente, las funciones pueden recibir más de un argumento. Por ejemplo:

# In[161]:


def mayor(a,b):
    m = a
    if a < b:
        m = b
    return m


# In[162]:


print( mayor(50,30) )
print( mayor(1100,3050) )


# La función `mayor` recibe dos valores numéricos y determina cuál es el mayor de ambos mediante 
# una comparación con la sentencia `if`. 
# 
# ¿Pueden las funciones en Python devolver más de un valor? ¡Claro! Hace falta nada más separar 
# con comas los valores a devolver.
# 

# In[163]:


def calcula_rectangulo(b,h):
    A = b*h
    P = 2*b + 2*h
    return A, P


# In[164]:


print( calcula_rectangulo(10,5) )
print( calcula_rectangulo(50,15) )


# También es posible guardar/asignar los valores devueltos por la función en variables:
# 

# In[165]:


area1, perimetro1 = calcula_rectangulo(100, 20)
print("Área: {0}\nPerímetro: {1}".format(area1, perimetro1))


# ### Funciones con una cantidad de parámetros indeterminada
# 
# En ocasiones el número de parámetros que deberá recibir una función no puede ser algo fijo. 
# Las definiciones de función en Python tienen la flexibilidad de poder recibir una cantidad 
# variable de argumentos de entrada. 
# 
# Para ejemplificar esto, vamos a crear una función llamada `promedio` que calcule 
# el promedio de una cierta cantidad de números pasados como argumentos:

# In[166]:


def promedio(*numeros):
    suma = 0
    k = 0
    for n in numeros:
        suma += n
        k += 1
    return suma/k


# In[167]:


print(promedio(10,5))
print(promedio(10,50,40,80,20,100))
print(promedio(5,15,10,5))


# Observe que lo único que hacemos es que al nombre del parámetro le anteponemos un asterisco, esto le indica 
# a Python que la cantidad de argumentos de entrada es indeterminada, en principio. Claro está, que el manejo posterior 
# de la información es algo que el programador debe tener en cuenta. Dentro del cuerpo de la función 
# se debe considerar que el parámetro `numeros` será una tupla cuya cantidad de elementos dependerá 
# de la cantidad de argumentos ingresados.

# ### Funciones y los argumentos con nombre
# 
# Una función en Python se puede *mandar a llamar* pasándo los argumentos de manera posicional, es 
# decir, en el orden que fueron definidos en la función, o bien, haciendo uso del nombre del parámetro correspondiente 
# al argumento que se introduce, por ejemplo:

# In[168]:


def cuenta_cuantas(frase, letra):
    k = 0
    for car in frase:
        if car is letra:
            k += 1
    return k


# In[169]:


print( cuenta_cuantas("hola mundo", "o") )
print( cuenta_cuantas(frase="hola mundo", letra="o") )
print( cuenta_cuantas(letra="o", frase="hola mundo") )


# La función `cuenta_cuantas` devuelve el número de presencias de una determinada letra en una frase. Observe 
# las tres formas en que la *ejecutamos*, todas son equivalentes. En la primera se pasan los argumentos de 
# forma posicional, en la segunda y tercera se utilizan los argumentos con nombres, note que en este caso el orden 
# en que los argumentos son pasados, es indistinto.
# 
# En la definición de funciones es posible también especificar que se pasarán ciertos argumentos con nombre 
# sin necesidad de escribirlos de manera explícita. Observe la siguiente función:

# In[170]:


def muestra_puntos(**personas):
    for persona in personas.items():
        print(persona[0] + " tiene " + str(persona[1]) + " puntos")


# In[171]:


muestra_puntos(Jorge=8, Paty=10)
print(30*"=")
muestra_puntos(Ana=6, Carlos=9, Victor=4, Daniela=8)


# Vea que la definición de la función `muestra_puntos` incluye un parámetro llamado `**personas`, esos dos 
# asteriscos antes del nombre del parámetro, indican que no se tiene predeterminado el número de argumentos que se 
# pasarán, pero además, indica que cada argumento a introducir deberá ser un argumento con nombre.
# Dentro del cuerpo de la función el parámetro `**personas` es un diccionario cuyas claves 
# son los nombres de los argumentos y los valores corresponden a cada valor asignado al argumento.
