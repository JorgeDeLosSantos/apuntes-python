# Interfaces gráficas con wxPython

## ¿Qué es wxPython?

## Lo básico

### Una primera aplicación

Una aplicación muy básica en wxPython puede construirse con unas pocas líneas:

```python
import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"wxPython Demo")
frame.Show()
app.MainLoop()
```

![Imagen 01](images/conceptos-elementales/primera_aplicacion.png)

Primero, y como siempre, importamos la librería wxPython para poder utilizar 
las clases y funciones disponibles en esta. 

Posteriormente se debe instanciar un objeto de la clase `wx.App`, que representa 
a la aplicación por si misma. La clase `wx.App` se utiliza para inicializar 
el sistema de wxPython y todo el conjunto de interfaces gráficas, además de controlar 
el intercambio de información y el manejo de los eventos lanzados. 
Cada aplicación debe tener una instancia `wx.App`, y esta debe crearse antes de 
instanciar cualquier otro objeto gráfico de wxPython, para asegurar que el 
sistema de wxWidgets se ha inicializado correctamente [^wxapp]. Es más, si en el ejemplo 
anterior intenta inicializar el Frame antes de `wx.App`, entonces wxPython lanzará un 
error como el que se muestra enseguida (*el cual es bastante explícito*):

```python
Traceback (most recent call last):
  File "C:\Users\adminIS\Desktop\LABPro\_books_\PB1703 - AWE\AWE\manuscript\src\
conceptos-elementales\primera_aplicacion.py", line 4, in <module>
    frame = wx.Frame(None, wx.ID_ANY, u"wxPython Demo")
  File "C:\Python27\lib\site-packages\wx-2.9.5-msw\wx\_windows.py", line 580, in
 __init__
    _windows_.Frame_swiginit(self,_windows_.new_Frame(*args, **kwargs))
wx._core.PyNoAppError: The wx.App object must be created first!
```

[^wxapp]: https://wxpython.org/docs/api/wx.App-class.html

Con la clase `wx.Frame` creamos un objeto de tipo **ventana**, que es donde colocaremos 
todos los controles que componen una interfaz gráfica. Para instanciar un objeto de la clase 
`wx.Frame`, necesitamos pasar algunos argumentos, por ejemplo, si recurrimos a la ayuda 
proporcionada por wxPython, respecto al constructor de `wx.Frame`:

```python
>>> help(wx.Frame.__init__)
Help on method __init__ in module wx._windows:

__init__(self, *args, **kwargs) unbound wx._windows.Frame method
  __init__(self, Window parent, int id=-1, String title=EmptyString, 
      Point pos=DefaultPosition, Size size=DefaultSize, 
      long style=DEFAULT_FRAME_STYLE, String name=FrameNameStr) -> Frame
```

wxPython nos *dice* que necesitamos especificar al menos el argumento `parent`, que es 
el *objeto padre* del Frame. En el ejemplo utilizado hemos pasado `None` como argumento, 
para indicar que nuestro objeto frame no tiene un objeto padre. Note que además de 
`parent`se puede especificar un `id`, un título (`title`), la posición (`position`), 
el tamaño (`size`), el estilo (`style`) y un nombre (`name`). En nuestro caso 
hemos pasado, además de `parent`, un `id` y un título (string que se muestra en la parte 
superior de la ventana). Si quisiera especificar un tamaño inicial al Frame podría incluirse 
el argumento `size` como sigue:


```python
frame = wx.Frame(None, wx.ID_ANY, u"wxPython Demo", size=(300,200))
```

El método `Show` de la clase `wx.Frame` se utiliza para mostrar en pantalla la ventana que hemos 
creado y todos los elementos que pudiera contener, si no *llamamos* a `Show` la ventana no 
se dibujará en la pantalla. Luego, el método `MainLoop` de `wx.App` es el que *pone en funcionamiento* 
toda la maquinaria de wxPython, lista para recibir y manejar los eventos generados.

### Con clase

En la sección anterior vimos como desarrollar una aplicación wxPython muy elemental, con unas 
cuantas líneas de código. Todo esto está muy bien, pero cuando querramos desarrollar una 
aplicación un poco más compleja vamos a tener muchos problemas con ese mismo enfoque. 
Además, cuando se requiera programar las respuestas a los eventos, se necesita mucho 
intercambio de información entre el objeto que lanza el evento y las funciones o rutinas 
que los manejan (handlers), y de esa manera, aun con la ayuda de las funciones es un tanto 
difícil mantener el código legible.

Debido a lo comentado en el párrafo anterior, las aplicaciones en wxPyhon comúnmente 
se desarrollan utilizando un diseño orientado a objetos, donde, típicamente se escriben 
clases heredadas de los controles gráficos de wxPython.

Lo más común, es crear una clase que herede de `wx.Frame`, y en esta ir agregando todos 
los controles gráficos que necesitemos para que la aplicación sea funcional.

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,parent,**kwargs):
        wx.Frame.__init__(self,parent=parent,**kwargs)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiFrame(None, title=u"wxFrame Demo")
    app.MainLoop()
```

Primero, definimos una clase MiFrame heredada de wx.Frame, agregamos el método `__init__` que 
para efectos de este texto será nuestro constructor de la clase, y aquí en `__init__` es 
necesario llamar también al método `__init__` de la superclase, pasándole como argumentos 
aquellos que hemos recibido desde el constructor de nuestra clase MiFrame. Note que, debido 
a la sintaxis de Python, el parámetro self será siempre el primer argumento del método `__init__` 
de la clase y superclase. Dentro del método `__init__` habrán de agregarse todos los controles 
(que veremos en la siguiente entrega) y hacer las conexiones de eventos requeridas. 
El método `Show` sirve, claro está, para mostrar el Frame en la pantalla.

Para llamar al método `__init__` de la superclase, también puede utilizar la otra 
notación que implica el uso de super, algo como:

```
super(MiFrame, self).__init__(*args,**kwargs)
```

Finalmente, lo único que hacemos es instanciar un objeto de la clase `MiFrame`, con los mismos 
argumentos que utilizaríamos para uno de `wx.Frame`. Y bueno, lo de la clase `wx.App` ya nos lo 
sabemos, puesto que lo hemos visto en la sección anterior.

## Los sizers: organizando controles

En este capítulo veremos cómo posicionar y organizar los controles mediante 
el uso de sizers, los cuales son mecanismos de distribución automática de 
controles gráficos mediante algoritmos de posicionamiento.

### Posicionamiento absoluto

El *posicionamiento absoluto* es la manera más sencilla para posicionar 
y organizar controles dentro de una interfaz gráfica de wxPython. Esto 
consiste en manejar de forma manual el tamaño y posición de los controles 
mediante las propiedades `size` y `pos`,  respectivamente. Revise el siguiente 
ejemplo.

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,parent,**kwargs):
        wx.Frame.__init__(self,parent=parent,**kwargs)
        self.bt1 = wx.Button(self, -1, u"Botón 1", pos=(50,60), size=(100,20))
        self.bt2 = wx.Button(self, -1, u"Botón 2", pos=(50,120), size=(100,20))
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiFrame(None, title=u"Posicionamiento absoluto", size=(300,200))
    app.MainLoop()
```

Puede notar que a los *keyword arguments* `pos` y `size` se les pasa una tupla de 
dos elementos, que indican las coordenadas *x* e *y* del extremo superior izquierdo 
del control gráfico en el caso de la posición, y el ancho y alto del mismo en el caso del tamaño, 
siendo en ambos casos pixeles las unidades de medida.