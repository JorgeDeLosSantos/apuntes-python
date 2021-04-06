#!/usr/bin/env python
# coding: utf-8

# # Introducción
# 
# 
# ## ¿Qué es Python?
# 
# Python es un lenguaje de programación, interpretado, de alto nivel y propósito general, además de ser un proyecto libre y de código abierto, con una comunidad enorme implicada en el desarrollo y mantenimiento de librerías que hacen posible el *multidominio* actual de Python.
# 
# Dada su concepción como lenguaje de propósito general, Python es utilizado en una diversidad de aplicaciones, 
# desde desarrollo web, encriptación, análisis de datos, procesamiento de imágenes, aprendizaje automático, 
# computación simbólica, etc.  
# 
# Las características de este lenguaje le hacen propicio para el prototipado de aplicaciones, dado que es muy 
# sencillo y rápido revisar y modificar el código desarrollado. Otra característica muy notable de Python 
# es su sintaxis simple y fácil de aprender, lo cual ayuda al momento de introducirse en el desarrollo de 
# algoritmos o el mundo propio de la programación de computadoras.
# 
# ## Instalando Python
# 
# En estos apuntes se utilizará la distribución Anaconda de Python, la cual contiene el intérprete y las librerías del 
# *core*, pero que además incluye la mayoría de librerías utilizadas para el desarrollo de aplicaciones de corte 
# técnico-científico.
# 
# La descarga de Anaconda puede realizarla desde el sitio https://www.anaconda.com/download/, selecciona el 
# paquete de descarga conforme al sistema operativo (Windows, macOS o Linux) así como la arquitectura de su PC.
# La instalación suele ser muy sencilla, puede seguir las instrucciones dadas en el *How to install ANACONDA* de 
# la misma página.

# ## El notebook de Jupyter como una calculadora básica
# 
# Una vez instalado Anaconda puede testear la correcta instalación abriendo el Jupyter Notebook, la cual es una aplicación web en la cual puede escribir código, texto, ecuaciones, etc., y que básicamente es donde se desarrollaron estos apuntes. Puede 
# buscar esta aplicación en la carpeta de instalación correspondiente.
# 
# A partir de este momento puede ingresar código Python en las celdas y teclear **Shift + Enter** para ejecutar la instrucción y la celda le devolverá lo que resulte de esto. Por ejemplo, si escribe un número cualesquiera y presiona la combinación indicada, la consola le devolverá justamente el mismo número:

# In[1]:


1000


# Puede ejecutar una simple suma aritmética:

# In[2]:


100 + 200


# O una resta:

# In[3]:


550 - 650


# Naturalmente Python maneja sin complicaciones las cantidades negativas. Una multiplicación la realiza 
# con el operador *:

# In[4]:


50*25


# Para las divisiones utiliza el operador /:

# In[5]:


1/2


# Puede elevar a una potencia utilizando como operador el doble asterisco:

# In[6]:


13**2


# Inclusive existe la posilidad de definir números complejos y realizar operaciones con ellos:

# In[7]:


5 + 2j


# In[8]:


(5 + 2j) - (10 + 7j)


# In[9]:


(5 + 2j)*(10 + 7j)


# Puede ampliar la capacidad de las funcionalidades *built-in* de Python si importa alguna librería, como `math`, pero claro, esto será un tema a tratar con posterioridad.
