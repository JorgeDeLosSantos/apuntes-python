import matplotlib.pyplot as plt
import numpy as np

base_dir = r"C:\Users\delos\Google Drive\Apuntes - Python\img\ch03\\"

def grafica_01a():
    plt.plot([0,1,2,3,4,5], [5,10,6,-10,15,1])

    plt.savefig(base_dir+"grafica_01a.pdf")
    plt.show()
    
def grafica_01b():
    plt.plot([0,1,2,3,4,5], [5,10,6,-10,15,1], 'r--o', label="Partícula 1")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")
    plt.title("Una primera aproximación")
    plt.text(2,7,"$ P_1 (2,6) $", color="b")
    plt.legend()
    plt.grid(ls="--", color="#dadada")
    plt.savefig(base_dir+"grafica_01b.pdf")
    plt.show()
    
    
def plot_one_argument():
    plt.plot([1,2,3,4,5])
    plt.savefig(base_dir+"plot_one_argument.pdf")
    plt.show()

def plot_two_argument():
    plt.plot([10,25,30,60,70,100], [100,200,-100,300,0,-250])
    plt.savefig(base_dir+"plot_two_argument.pdf")
    plt.show()

def plot_function():
    x = np.linspace(0, 30)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x,y)
    plt.savefig(base_dir+"plot_function.pdf")
    plt.show()


def plot_function_less_points():
    x = np.linspace(0, 30, 5)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x,y)
    plt.savefig(base_dir+"plot_function_less_points.pdf")
    plt.show()


def plot_function_more_points():
    x = np.linspace(0, 30, 1000)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x,y)
    plt.savefig(base_dir+"plot_function_more_points.pdf")
    plt.show()


def plot_color_and_style():
    x = np.linspace(0, 30)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, "r--")
    plt.savefig(base_dir+"plot_color_and_style.pdf")
    plt.show()

def plot_color_and_style_02():
    x = np.linspace(0, 30)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, "go")
    # plt.savefig(base_dir+"plot_color_and_style_02.pdf")
    plt.show()

def plot_color_and_style_03():
    x = np.linspace(0, 30)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, linestyle="-", color="coral", marker="*")
    plt.savefig(base_dir+"plot_color_and_style_03.pdf")
    plt.show()

def plot_color_and_style_04():
    x = np.linspace(0, 30)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, linestyle="-", color="coral", marker="*", linewidth=3)
    plt.savefig(base_dir+"plot_color_and_style_04.pdf")
    plt.show()


def plot_xlabel_ylabel_title():
    x = np.linspace(0, 30, 500)
    y1 = np.exp(-0.1*x)*np.cos(x)
    y2 = np.exp(-0.2*x)*np.sin(x)
    plt.plot(x, y1, "b-", label="Partícula 1")
    plt.plot(x, y2, "r-", label="Partícula 2")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (mm)")
    plt.title("Gráfica de posición")
    plt.legend()
    plt.savefig(base_dir+"plot_xlabel_ylabel_title.pdf")
    plt.show()
    

def plot_text():
    x = np.linspace(0, 30, 200)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, "m")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (mm)")
    plt.title("Gráfica de posición")
    plt.text(10, 0.5, "Algo informativo")
    plt.savefig(base_dir+"plot_text.pdf")
    plt.show()
    

def plot_text_2():
    x = np.linspace(0, 30, 200)
    y = np.exp(-0.1*x)*np.cos(x)
    plt.plot(x, y, "m")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (mm)")
    plt.title("Gráfica de posición")
    plt.text(10, 0.5, "Algo informativo", fontsize=16, color="r", 
             name="Courier New")
    plt.savefig(base_dir+"plot_text_2.pdf")
    plt.show()
    



if __name__ == "__main__":
    plot_text_2()
