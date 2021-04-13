#!/usr/bin/env python
# coding: utf-8

# # Estructuras de control

# En un lenguaje de programación, las estructuras de control permiten modificar el flujo de la ejecución de un conjunto de instrucciones. Se pueden distinguir tres tipos básicos de control de flujo, a saber:
# 
# * Control secuencial
# * Control de selección
# * Control de repetición

# ![](img/estructuras-de-control/estructuras-de-control.svg)

# En el control secuencial las instrucciones se ejecutan de manera secuencial desde el inicio hasta el fin del programa. En el control de selección se tiene una condición que puede ser falsa o verdadera, dependiendo de esto se ejecutará uno u otro bloque de instrucciones. En el control de repetición, un bloque de instrucciones se ejecuta de manera repetitiva mientras una condición sea verdadera, en caso contrario el flujo de ejecución se pasará a otro conjunto de instrucciones.

# ## Condicional `if-elif-else`
# 
# El condicional `if-elif-else` es una estructura de control de selección que sirve para *tomar decisiones*, basándose en la evaluación de condiciones y/o comparaciones, en el flujo del programa. La sintaxis más general para `if-elif-else` es:
# 
# ```python
# if cond1:
#     # hacer algo 
# elif cond2:
#     # hacer otra cosa
# ...
# elif condn:
#     # hacer algo más
# else:
#     # hacer algo por default
# ```
# 
# Donde `cond1, cond2, ... condn` son valores lógicos que resultan de una comparación. Esta estructura se evalúa 
# secuencialmente hasta encontrar una condición que se cumpla, si ninguna lo hace, entonces se ejecuta la instrucción 
# colocada en el caso por default `else`.
# 
# Hay que tener especial cuidado con las indentaciones de los bloques de código, en Python las indentaciones no son opcionales, tienen un significado sintáctico. La mayoría de los editores de código de Python indentarán de manera automática la siguiente línea, cada vez que coloques los dos puntos al final de una línea.

# En el siguiente fragmento de código se muestra un programa que verifica si el valor de `a` es mayor, menor o igual al valor de `b`.

# In[2]:


a = 10
b = 30

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")


# Es muy común que en algunos casos, por cuestiones inherentes a lo que se está programando, únicamente se decida entre dos posibilidades que son excluyentes, en esos casos basta con una estructura *reducida* `if-else`.
# 
# Por ejemplo, el siguiente código determina si un número es par o impar (un número entero cualquiera o es par o es impar, no hay otra posibilidad).

# In[3]:


n = 1001

if (-1)**(n) > 0:
    print("El número es par")
else:
    print("El número es impar")


# La verificación que realiza el código anterior se basa en el hecho de que las potencias pares de -1 siempre serán 1, y las impares -1, es decir:
# 
# $$
# (-1)^n = \left\{\begin{matrix}
# 1 \text{       ; si n es par} \\
# -1 \text{      ; si n es impar} 
# \end{matrix}\right.
# $$

# Supongamos ahora otro caso en donde las posibilidades son mutuamente excluyentes: en un curso la calificación mínima aprobatoria es de 70, la escala de calificación es de 0 a 100, ¿cómo podríamos implementar un código que decida si un alumno aprobó o reprobó la asignatura? Observa lo siguiente:

# In[16]:


calificacion = 100

if calificacion >= 70:
    print("Aprobado")
else:
    print("No aprobado")


# ```{admonition} Sobre datos y validaciones
# :class: warning
# 
# Usualmente un programa de computadora recibe datos de forma externa, es decir, alguien los proporciona de forma manual o se leen desde algún archivo de datos o desde algún sensor. Esto implica la posibilidad de que se reciban datos que no corresponderían con lo esperado, por ejemplo, en el caso del programa anterior, imagina ¿qué pasaría si un usuario inserta una calificación de 150? El programa seguiría funcionando y te imprimiría un mensaje de aprobado. Una manera de solventar esta situación sería adicionar una  verificación de que el valor pasado esté en el rango de valores esperado, por ejemplo:
# 
# 
# ```python
# calificacion = 150
# 
# if calificacion < 0 or calificacion > 100:
#     print("La calificación debe estar en la escala de 0 a 100")
# elif calificacion >= 70:
#     print("Aprobado")
# else:
#     print("No aprobado")
# ```
# ```

# ## Ciclo `for`
# 
# El **bucle for** es una estructura de control de repetición, en la cual se conocen 
# *a priori* el número de iteraciones a realizar. En lenguajes como C++ o Java, el ciclo `for` 
# necesita de una variable de ciclo de tipo entero que irá incrementándose en cada iteración. En Python, la cuestión es un poco diferente, el ciclo `for` *recorre* una secuencia y en la k-ésima iteración la variable de ciclo *adopta* el 
# valor del elemento en la k-ésima posición del iterable.
# 
# De manera general, la sintaxis de `for` es:
# 
# ```python
# for var in secuencia:
#     # Hacer algo ...
# ```
# 
# Donde `var` es la **variable de ciclo** o **variable de control** y `secuencia` la secuencia de valores que deberá iterarse. Es necesario remarcar la importancia de los dos puntos al final de esta primera línea y en indentar el bloque de 
# código subsecuente que definirá el cuerpo del ciclo for.

# Como primer ejemplo vamos a recorrer una lista de números y mostrarlos por consola:

# In[17]:


numeros = [18,50,90,-20,100,80,37]
for n in numeros:
    print(n)


# Observe que en cada iteración la variable de ciclo `n` adopta el valor de cada uno de los elementos de la 
# lista `numeros`.
# 
# Como ya se mencionó, en Python la variable de ciclo no necesariamente adopta valores numéricos enteros secuenciales, 
# si no valores dentro de una secuencia. Esta secuencia podría ser también una cadena de caracteres, por ejemplo:

# In[148]:


palabra = "Python"
for letra in palabra:
    print(letra)


# Dentro de un ciclo for podemos colocar cualquier otra instrucción de control de flujo. Un caso muy común es el de incluir otro ciclo for, algo que habitualmente se denota como **ciclos anidados**. Por ejemplo, supongamos que se requieren mostrar por consola todos los elementos de algunas listas contenidas dentro de otra lista principal, en ese caso se hace necesario primero iterar sobre la lista principal y enseguida hacerlo sobre las listas contenidas, por ejemplo:

# In[18]:


matriz = [[-5,2,0], [9,5,6], [1,7,15]]
for fila in matriz:
    for elemento in fila:
        print(elemento)


# Con un ciclo for también podemos *desempaquetar* múltiples valores:

# In[19]:


puntos = [(0,0), (1,0), (1,1), (0,1)]

for x,y in puntos:
    print(f"x={x} y={y}")


# Una forma equivalente de *desempaquetar* el conjunto de tuplas anteriores sería como sigue:

# In[24]:


puntos = [(0,0), (1,0), (1,1), (0,1)]

for punto in puntos:
    print(f"x={punto[0]} y={punto[1]}")


# Observa la diferencia, la primera forma es un quizá un poco menos *intuitiva* pero más práctica y natural. En la primera se accede directamente con las variables de ciclo `(x,y)` a cada elemento de las tuplas que conforman la lista `puntos`, con la segunda se tiene que acceder mediante indexación a cada elemento.

# ## Ciclo `while`

# El ciclo `while` ejecuta un bloque de instrucciones mientras haya una condición que se cumpla. La sintaxis de `while` es: 
# 
# ```python
# while cond:
#     # hacer algo 
# ```
# 
# Donde `cond` es un valor de tipo booleano que usualmente resulta de realizar una comparación; mientras `cond` sea un valor booleano `True` entonces el bloque de instrucciones contenidas en `while` se ejecutarán.
# 
# Veamos un ejemplo:

# In[25]:


x = 1
while x < 5:
    print(x)
    x += 1


# En el código anterior, inicialmente `x` tiene un valor de 1, el flujo del programa *entra* en el ciclo while, puesto que la condición se cumple (dado que en ese momento `1 < 5`), posteriormente se ejecutan de manera repetitiva las instrucciones que están dentro del ciclo while, hasta que `x = 5`. La instrucción `x += 1` suma 1 al valor de `x` en cada iteración. 

# Aunque es menos común y poco práctico, con `while` podríamos iterar, como con `for`, sobre una secuencia:

# In[34]:


nombre = "Pablo"
k = 0
while k < len(nombre):
    print(nombre[k])
    k += 1


# El ciclo `while` suele ser muy utilizado en métodos numéricos, donde el número de iteraciones requeridas puede establecerse por el usuario de manera directa o bien mediante la indicación de una tolerancia.

# Por ejemplo, el [método de Newton](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Newton) es un algoritmo que se utiliza para aproximar  raíces de una función real. Este método se puede establecer como sigue: 
# 
# > Sea $f$ una función real derivable, y sea r un cero real de $f$. Si $x_n$ es una aproximación a $r$, 
# > entonces la siguiente aproximación $x_{n+1}$ está dada por:
# >
# > $$ x_{n+1} = x_n - \frac{ f(x_n) }{ f'(x_n) } $$
# >
# > Donde $ f' $ denota la derivada de $ f $. [^newton]
# 
# [^newton]: https://www.calculo.jcbmat.com/id454.htm

# Vamos a aproximar una de las raíces de la función $ f(x) =  x^3 - 5x^2 + 3$, para ello necesitamos conocer también la derivada de esta función, derivando se tiene que $f'(x) = 3x^2 - 10x$. Observe el siguiente código implementado:

# In[44]:


f = lambda x: x**3 - 5*x**2 + 3 # función f
fp = lambda x: 3*x**2 - 10*x # derivada de la función f'
nit = 5 # número de iteraciones
k = 0 # contador de iteraciones
xn = 0.5 # valor inicial

while k < nit:
    xnm1 = xn - ( f(xn) / fp(xn) )
    xn = xnm1
    k += 1
    print(f"N = {k} | xn = {xn}")


# En `f` y `fp` se definen como funciones lambda las expresiones correspondientes a la función y su derivada, de manera respectiva. En la variable `nit` establecemos el número de iteraciones a realizar, la variable `k` funciona como un contador de iteraciones y en `xn` se guarda primeramente el valor inicial, y posteriormente, cada una de las aproximaciones realizadas. 

# Ahora veamos otro ejemplo, en donde se combina el uso de `while` con el condicional `if-else`.

# In[25]:


from random import randint

print("¡Bienvenido a Adivina el Número!")
n = randint(1,10) # Genera un entero aleatorio en el intervalo [1,10]
k = 1 # número de intentos

while True:
    x = int( input("Ingrese un entero entre 1 y 10: ") )
    if x == n:
        print(f"Has adivinado después de {k} intentos")
        break
    else:
        print(f"{x} no es el número, intenta nuevamente\n")
    k += 1


# El código anterior es un juego muy simple de adivinar un número entero entre 1 y 10 que la computadora genera de manera aleatoria mediante la función `randint`. Observa que el ciclo `while`, en principio, se ejecutará de forma indefinida, dado que la condición es la constante booleana `True`; en este caso para *romper* la ejecución iterativa se hace uso de la instrucción `break`, en conjunto con la sentencia de selección `if-else`, observa que si la condición del `if` se cumple (`x == n`) entonces el programa rompe el ciclo `while` con la instrucción `break`, en caso contrario simplemente se sigue ejecutando el juego.

# ## Ejercicios

# ---
# 1. Desarrolle un programa que calcule la suma de los enteros del 1 al 100, es decir: 1 + 2 + 3 + ... + 99 + 100

# ---
# 2. Escriba un programa que reciba un entero positivo. Sí el número ingresado es múltiplo de 5 deberá imprimir en pantalla `El número es múltiplo de 5`, en cualquier otro caso deberá imprimir `El número no es múltiplo de 5`.

# ---
# 3. Escriba un programa que reciba como entrada una frase (un string) y determine cuántas veces aparece cada una de las vocales en esa frase. El valor de salida a mostrar debe ser un diccionario, se muestra enseguida un ejemplo:
# 
# ```python
# # entrada
# frase = "hola mundo"
# 
# # salida
# {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}
# ```
# 
# 

# ---
# 4. Desarrolle un programa que reciba una lista de números enteros y calcule cuántos el porcentaje de números pares que contiene, redondee el porcentaje calculado. 
# 
# ```python
# # Ejemplos
# 
# x = [10,20,40,45,66,53,55] # porcentaje -> 57
# x = [100,200,300] # porcentaje -> 100
# x = [33,45,65,90,23,12,189] # porcentaje -> 29
# ```

# ---
# 5. ¿Cuál es el error en el siguiente código? Descríbalo.

# In[1]:


numeros = [10,20,30]
for x,y in numeros:
    print(x)


# ---
# 6. Modifique el siguiente código para que se muestre en pantalla lo siguiente:
# 
# ```
# x
# xx
# xxx
# xxxx
# xxxxx
# ```

# In[16]:


for x in range(1,3):
    print(x * "o")


# 
