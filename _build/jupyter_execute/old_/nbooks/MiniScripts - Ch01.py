#!/usr/bin/env python
# coding: utf-8

# In[57]:


edades = {"Ana": 25, "David": 18, "Lucas": 35, "Ximena": 30, "Ale": 20}


# In[54]:


edades["Ana"]


# In[60]:


edades.pop("Ana")


# In[61]:


edades


# ## Funciones

# In[1]:


def saluda(nombre):
    s = "Hola " + nombre + ", bienvenido."
    return s

print(saluda("Jorge"))


# In[1]:


def espar(n):
    if n%2 == 0:
        s = True
    else:
        s = False
    return s

print(espar(2))
print(espar(5))
print(espar(10))


# In[7]:


def mayor(a,b):
    m = a
    if a < b:
        m = b
    return m

print( mayor(50,30) )
print( mayor(1100,3050) )


# In[14]:


def calcula_rectangulo(b,h):
    A = b*h
    P = 2*b + 2*h
    return A, P

print( calcula_rectangulo(10,5) )
print( calcula_rectangulo(50,15) )


# In[41]:


area1, perimetro1 = calcula_rectangulo(100, 20)
print("Área: {0}\nPerímetro: {1}".format(area1, perimetro1))


# In[52]:


def mayor(*numeros):
    m = numeros[0]
    for numero in numeros:
        if numero > m:
            m = numero
    return m


# In[51]:


mayor(4,3,6,5)


# In[75]:


def promedio(*numeros):
    suma = 0
    k = 0
    for n in numeros:
        suma += n
        k += 1
    return suma/k

print(promedio(10,5))
print(promedio(10,50,40,80,20,100))
print(promedio(5,15,10,5))


# In[5]:


def cuenta_cuantas(frase, letra):
    k = 0
    for car in frase:
        if car is letra:
            k += 1
    return k

print( cuenta_cuantas("hola mundo", "o") )
print( cuenta_cuantas(frase="hola mundo", letra="o") )
print( cuenta_cuantas(letra="o", frase="hola mundo") )


# In[17]:


def muestra_puntos(**personas):
    for persona in personas.items():
        print(persona[0] + " tiene " + str(persona[1]) + " puntos")

muestra_puntos(Jorge=8, Paty=10)
print(30*"=")
muestra_puntos(Ana=6, Carlos=9, Victor=4, Daniela=8)


# ## Estructuras de control
# 
# ### Ciclo for

# In[1]:


numeros = [18,50,90,-20,100,80,37]
for n in numeros:
    print(n)


# In[2]:


palabra = "Python"
for letra in palabra:
    print(letra)


# In[6]:


matriz = [[-5,2,0], [9,5,6], [1,7,15]]
for fila in matriz:
    for elemento in fila:
        print(elemento)


# In[34]:


a = 0
b = 10
n = 100
f = "x"
dx = (b-a)/n
A = 0
xi = a + dx
while xi <= b:
    x = xi
    A += eval(f)*(xi-(xi-dx))
    xi += dx


# In[49]:


palabras = ["Carro", "Sol", "Mesa", "Dinosaurio", "Girasol", "Silla"]
for palabra in palabras:
    print(len(palabras))


# ## If

# In[ ]:


if cond1:
    # hacer algo 
elif cond2:
    # hacer otra cosa
    #.
    #.
    #.
elif condn:
    # hacer algo más
else:
    # hacer algo por default

